#!/usr/bin/env python3
import json
import os
from glob import glob
from pathlib import Path
from typing import List
import typer
import yaml
from rich import print

app = typer.Typer(add_completion=False)

def _discover_specs() -> List[str]:
    env_specs = os.getenv("OPENAPI_SPECS")
    if env_specs:
        items = [s.strip() for s in env_specs.split(",") if s.strip()]
        if items:
            return items
    patterns = [
        "specs/openapi.yaml", "specs/openapi.yml", "specs/openapi.json",
        "openapi.yaml", "openapi.yml", "openapi.json",
        "swagger.yaml", "swagger.yml", "swagger.json",
        "**/*openapi*.yaml", "**/*openapi*.yml", "**/*openapi*.json",
        "**/swagger*.yaml", "**/swagger*.yml", "**/swagger*.json",
    ]
    candidates: List[str] = []
    for pat in patterns:
        for m in glob(pat, recursive=True):
            if any(seg in m.replace("\\", "/").split("/") for seg in ["node_modules", ".git", ".tester"]):
                continue
            candidates.append(m)
    uniq: List[str] = []
    seen = set()
    for c in candidates:
        p = str(Path(c))
        if p not in seen and Path(p).is_file():
            seen.add(p)
            uniq.append(p)
    return uniq


@app.command()
def main(
    spec: List[str] = typer.Option(None, "--spec", help="OpenAPI spec file path or URL. Can be repeated."),
    out: str = typer.Option(".tester/workflows/proposals.yaml", help="Output proposals YAML"),
):
    """
    Deterministic analyzer stub: emits simple CRUD-like workflow proposals from the spec names.
    GenAI (Bedrock) can be integrated later; we gate it via env vars to avoid accidental calls.
    """
    Path(out).parent.mkdir(parents=True, exist_ok=True)

    # Resolve specs (optional via discovery)
    specs = spec or []
    if not specs:
        print("[cyan]No --spec provided. Attempting auto-discovery...[/cyan]")
        specs = _discover_specs()
        if specs:
            print(f"[green]Discovered specs:[/green] {specs[:3]}{' ...' if len(specs)>3 else ''}")
        else:
            print("[red]No OpenAPI spec found. Set OPENAPI_SPECS env or pass --spec.")
            raise typer.Exit(2)

    # Minimal stub proposals
    proposals = {"workflows": []}
    for i, s in enumerate(specs, start=1):
        proposals["workflows"].append({
            "id": f"wf_{i:03d}",
            "title": f"Basic lifecycle for spec {Path(s).name}",
            "steps": [
                {"method": "POST", "path": "/resource", "save": {"resource_id": "$.body.id"}},
                {"method": "GET", "path": "/resource/{resource_id}"},
                {"method": "DELETE", "path": "/resource/{resource_id}"},
                {"method": "GET", "path": "/resource/{resource_id}", "expect_status": 404},
            ],
            "assertions": ["status per spec", "schema match"],
        })

    with open(out, "w", encoding="utf-8") as f:
        yaml.safe_dump(proposals, f, sort_keys=False)

    print(f"[green]Proposals written to[/green] {out}")

if __name__ == "__main__":
    app()
