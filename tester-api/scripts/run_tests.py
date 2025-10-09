#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path
import typer
from rich import print

app = typer.Typer(add_completion=False)

@app.command()
def main(
    collection: str = typer.Option(..., help="Path to Postman collection JSON"),
    env: str = typer.Option(None, help="Path to Newman environment JSON"),
    reporters: str = typer.Option("cli,junit", help="Comma-separated Newman reporters"),
    report_dir: str = typer.Option(".tester/reports", help="Output directory for reports"),
):
    """Run Newman on a Postman collection. Filtering by tags/folders can be added later."""
    Path(report_dir).mkdir(parents=True, exist_ok=True)

    cmd = ["npx", "--yes", "newman", "run", collection, "--reporters", reporters]

    if env:
        cmd += ["--environment", env]

    # JUnit and HTML defaults
    cmd += ["--reporter-junit-export", str(Path(report_dir) / "junit.xml")]

    print(f"[cyan]Running Newman:[/cyan] {' '.join(cmd)}")
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as e:
        print(f"[red]Newman failed with code {e.returncode}[/red]")
        raise SystemExit(e.returncode)

    print(f"[green]Reports at:[/green] {report_dir}")

if __name__ == "__main__":
    app()
