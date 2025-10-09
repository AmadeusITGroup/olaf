#!/usr/bin/env python3
import json
import os
import subprocess
import sys
from glob import glob
from pathlib import Path
from typing import List
import typer
from rich import print

app = typer.Typer(add_completion=False)

def _discover_specs() -> List[str]:
    """Discover OpenAPI specs via env or common file patterns."""
    # 1) Env var
    env_specs = os.getenv("OPENAPI_SPECS")
    if env_specs:
        items = [s.strip() for s in env_specs.split(",") if s.strip()]
        if items:
            return items

    # 2) Common local paths
    candidates: List[str] = []
    patterns = [
        "specs/openapi.yaml", "specs/openapi.yml", "specs/openapi.json",
        "openapi.yaml", "openapi.yml", "openapi.json",
        "swagger.yaml", "swagger.yml", "swagger.json",
        "**/*openapi*.yaml", "**/*openapi*.yml", "**/*openapi*.json",
        "**/swagger*.yaml", "**/swagger*.yml", "**/swagger*.json",
    ]
    for pat in patterns:
        for m in glob(pat, recursive=True):
            # Skip node_modules and .git
            if any(seg in m.replace("\\", "/").split("/") for seg in ["node_modules", ".git", ".tester"]):
                continue
            candidates.append(m)
    # Deduplicate preserving order
    seen = set()
    uniq = []
    for c in candidates:
        p = str(Path(c))
        if p not in seen and Path(p).is_file():
            seen.add(p)
            uniq.append(p)
    return uniq


@app.command()
def main(
    spec: List[str] = typer.Option(None, "--spec", help="OpenAPI spec file path or URL. Can be repeated."),
    out: str = typer.Option(".tester/postman/base.collection.json", help="Output Postman collection path"),
    portman_config: str = typer.Option("tester-api/config/portman.config.json", help="Portman config JSON"),
):
    """Build a Postman collection from OpenAPI using Portman (Path B)."""
    Path(out).parent.mkdir(parents=True, exist_ok=True)

    specs = spec or []
    if not specs:
        print("[cyan]No --spec provided. Attempting auto-discovery...[/cyan]")
        specs = _discover_specs()
        if specs:
            print(f"[green]Discovered specs:[/green] {specs[:3]}{' ...' if len(specs)>3 else ''}")
        else:
            print("[red]No OpenAPI spec found. Set OPENAPI_SPECS env or pass --spec.")
            raise typer.Exit(2)

    primary_spec = specs[0]
    if len(specs) > 1:
        print("[yellow]Multiple specs discovered/provided. Processing the first one only for now.[/yellow]")

    cmd = [
        "npx", "--yes", "@apideck/portman",
        "--openapi", primary_spec,
        "--postmanCollection", out,
        "--portmanConfig", portman_config,
    ]

    print(f"[cyan]Running Portman:[/cyan] {' '.join(cmd)}")
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as e:
        print(f"[red]Portman failed with code {e.returncode}[/red]")
        raise SystemExit(e.returncode)

    print(f"[green]Collection generated:[/green] {out}")

if __name__ == "__main__":
    app()
