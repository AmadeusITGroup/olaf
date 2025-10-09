from pathlib import Path
import json
import os
import sys
import time
from collections import deque

"""
Batch convert prompts in `olaf-core/prompts/treat-change-request/` using
`prompt-engineer/convert-prompt-existing.md`.

Spawns one agent per source prompt in parallel (background processes) via the
OLAF Strands API. Each spawned agent receives a per-file JSON context and the
protocol is forced to Act (no confirmations). The wrapper injects
BYPASS_TOOL_CONSENT=true; we also set it here redundantly.
"""

def _load_api(project_root: Path):
    """Load OLAFStrandsAPI from olaf-core/tools/strands without requiring package installs."""
    strands_dir = project_root / "olaf-core" / "tools" / "strands"
    if not strands_dir.exists():
        raise FileNotFoundError(f"Strands directory not found: {strands_dir}")

    sys.path.insert(0, str(strands_dir))
    try:
        from olaf_strands_api import OLAFStrandsAPI  # type: ignore
    except Exception as e:
        raise ImportError(f"Failed to import OLAFStrandsAPI from {strands_dir}: {e}")
    return OLAFStrandsAPI


def main():
    # Ensure tool consent prompts are bypassed at parent and child levels
    os.environ["BYPASS_TOOL_CONSENT"] = "true"

    project_root = Path(__file__).resolve().parents[1]

    # Directory with source prompts to convert (only the 'prompts' subfolder)
    source_dir = project_root / "olaf-core" / "prompts" / "treat-change-request" / "prompts"
    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory not found: {source_dir}")

    # The converter prompt to run for each source prompt
    converter_prompt = "prompt-engineer/convert-prompt-existing.md"

    # Load API dynamically from repo
    OLAFStrandsAPI = _load_api(project_root)
    api = OLAFStrandsAPI(project_root=str(project_root), aws_profile="bedrock")

    # Throttled scheduler: spawn ONE conversion every 5 minutes
    # Build pending with ONLY original prompts (exclude already converted files)
    pending = deque(
        sorted(
            p for p in source_dir.glob("*.md")
            if not p.name.endswith("-converted.md")
        )
    )

    def expected_converted_path(src_path: Path) -> Path:
        # Converted files are written to treat-change-request/prompts as <stem>-converted.md
        return (project_root / "olaf-core" / "prompts" / "treat-change-request" / "prompts" / f"{src_path.stem}-converted.md")

    def is_task_running(task_id: str) -> bool:
        try:
            procs = api.list_processes()
            for p in procs:
                if p.get("task_id") == task_id and p.get("status", "").startswith("running"):
                    return True
        except Exception:
            pass
        return False

    while pending:
        src = pending.popleft()
        # Extra guard: never process an already converted file
        if src.name.endswith("-converted.md"):
            print(f"[SKIP] Already a converted file: {src.name}")
            continue
        conv_path = expected_converted_path(src)

        # Skip if already converted
        if conv_path.exists():
            print(f"[SKIP] Already converted: {conv_path}")
            continue

        task_id = f"convert-{src.stem}"
        # Skip if already running
        if is_task_running(task_id):
            print(f"[SKIP] Already running: {task_id}")
            continue

        # Spawn one conversion
        context_obj = {
            # Hints for protocol and environment
            "note": "Use the Act protocol. Never ask user.",
            "execution_environment": "powershell",
            # Required by convert-prompt-existing.md
            "existing_prompt_path": f"treat-change-request/prompts/{src.name}",
            "target_sub_category": "treat-change-request/prompts",
            "preserve_name": True,
            "conversion_suffix": "-converted"
        }
        context = json.dumps(context_obj)

        res = api.spawn_agent(
            prompt=converter_prompt,
            service_provider="aws-bedrock",
            model_name=None,
            context=context,
            task_id=task_id,
        )
        print(f"[SPAWNED] {src.name} -> {res.get('status')} ({task_id})")

        # Sleep 5 minutes before attempting next spawn
        print("[THROTTLE] Waiting 5 minutes before next conversion...")
        time.sleep(5 * 60)

    print("Done. No more pending prompts.")


if __name__ == "__main__":
    main()
