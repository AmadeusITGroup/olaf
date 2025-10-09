#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path
import typer
import yaml
from rich import print

app = typer.Typer(add_completion=False)

@app.command()
def main(
    proposal_id: str = typer.Option(..., "--proposal-id", help="Workflow ID from proposals.yaml"),
    proposals: str = typer.Option(".tester/workflows/proposals.yaml", help="Proposals YAML path"),
    engine: str = typer.Option("postman", help="Engine for generated artifacts: postman"),
    collection_out: str = typer.Option(".tester/postman/workflows/workflow.collection.json", help="Output collection path"),
    mermaid_out: str = typer.Option(".tester/diagrams/", help="Directory to write Mermaid files & images"),
    docs_out: str = typer.Option("docs/workflows/", help="Directory for Markdown reports"),
):
    """Generate workflow-specific artifacts: Postman collection, Mermaid diagram, and Markdown report."""
    with open(proposals, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    wf = next((w for w in data.get("workflows", []) if w.get("id") == proposal_id), None)
    if not wf:
        print(f"[red]Workflow {proposal_id} not found in {proposals}[/red]")
        raise SystemExit(2)

    Path(collection_out).parent.mkdir(parents=True, exist_ok=True)
    Path(mermaid_out).mkdir(parents=True, exist_ok=True)
    Path(docs_out).mkdir(parents=True, exist_ok=True)

    # 1) Simple Postman collection with ordered items
    collection = {
        "info": {"name": f"Workflow {proposal_id}", "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"},
        "item": []
    }
    # Variable storage in collection-level variables
    collection["variable"] = [{"key": "baseUrl", "value": "{{baseUrl}}"}]

    for idx, step in enumerate(wf.get("steps", []), start=1):
        name = f"{idx:02d} {step.get('method')} {step.get('path')}"
        url = "{{baseUrl}}" + step["path"]
        request = {
            "name": name,
            "request": {
                "method": step["method"],
                "url": {"raw": url, "host": ["{{baseUrl}}"], "path": step["path"].lstrip("/").split("/")},
            }
        }
        # Basic test stub
        tests = [
            "pm.test(\"status is ok\", function () { pm.response.to.be.success; });"
        ]
        if "expect_status" in step:
            tests.append(f"pm.test(\"status is {step['expect_status']}\", function () {{ pm.response.to.have.status({step['expect_status']}); }});")
        event = [{"listen": "test", "script": {"exec": tests, "type": "text/javascript"}}]
        request["event"] = event

        # Save variables from response
        if step.get("save"):
            for var, jsonpath in step["save"].items():
                tests.append(
                    "pm.test(\"save var\", function () { try { var v = pm.response.json().id; pm.environment.set('" + var + "', v); } catch(e) {} });"
                )
        # Path param substitution is left to Postman variables; users may adjust pre-request scripts.

        collection["item"].append(request)

    with open(collection_out, "w", encoding="utf-8") as f:
        json.dump(collection, f, indent=2)
    print(f"[green]Postman collection written:[/green] {collection_out}")

    # 2) Mermaid sequence diagram
    mmd = ["sequenceDiagram", "    participant Client", "    participant API"]
    for step in wf.get("steps", []):
        m = step.get("method", "GET")
        p = step.get("path", "/")
        mmd.append(f"    Client->>API: {m} {p}")
    mmd_name = f"{proposal_id}.mmd"
    mmd_path = Path(mermaid_out) / mmd_name
    with open(mmd_path, "w", encoding="utf-8") as f:
        f.write("\n".join(mmd) + "\n")
    print(f"[green]Mermaid diagram written:[/green] {mmd_path}")

    # Render PNG via Mermaid CLI if available
    try:
        subprocess.check_call(["npx", "--yes", "mmdc", "-i", str(mmd_path), "-o", str(mmd_path.with_suffix('.png'))])
        print(f"[green]Mermaid PNG rendered:[/green] {mmd_path.with_suffix('.png')}")
    except Exception:
        print("[yellow]Mermaid CLI not available; skipped PNG rendering.[/yellow]")

    # 3) Markdown report
    md_path = Path(docs_out) / f"{proposal_id}.md"
    md = [
        f"# {wf.get('title', proposal_id)}",
        "",
        f"- **[id]** {proposal_id}",
        f"- **[collection]** {collection_out}",
        f"- **[diagram]** {mmd_path}",
        "",
        "## Steps",
    ]
    for i, step in enumerate(wf.get("steps", []), start=1):
        md.append(f"- **[{i:02d}]** {step.get('method')} {step.get('path')}")
    md.append("\n## Assertions\n")
    for a in wf.get("assertions", []):
        md.append(f"- **[assert]** {a}")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    print(f"[green]Markdown written:[/green] {md_path}
")

    # 4) Update index
    index_path = Path(docs_out) / "INDEX.md"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    existing = []
    if index_path.exists():
        existing = index_path.read_text(encoding="utf-8").splitlines()
    entries = [line for line in existing if line.startswith("- ")]
    link_line = f"- **[{proposal_id}]** {wf.get('title', proposal_id)} — {md_path.name}"
    if link_line not in entries:
        entries.append(link_line)
    index = ["# Workflows Index", ""] + sorted(entries)
    index_path.write_text("\n".join(index) + "\n", encoding="utf-8")
    print(f"[green]Index updated:[/green] {index_path}")

if __name__ == "__main__":
    app()
