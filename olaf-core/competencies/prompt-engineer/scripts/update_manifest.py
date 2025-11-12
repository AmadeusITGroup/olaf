#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

def load_manifest(manifest_path: Path):
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERROR: Manifest not found: {manifest_path}", file=sys.stderr)
        sys.exit(2)
    except json.JSONDecodeError as e:
        print(f"ERROR: Manifest JSON invalid: {manifest_path}: {e}", file=sys.stderr)
        sys.exit(2)

def save_manifest(manifest_path: Path, data: dict):
    tmp = manifest_path.with_suffix('.json.tmp')
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    tmp.replace(manifest_path)


def parse_aliases(s: str):
    if not s:
        return []
    return [a.strip() for a in s.split(',') if a.strip()]


def upsert_entry_point(m: dict, entry: dict):
    eps = m.setdefault('entry_points', [])
    # Try update existing by id
    for ep in eps:
        if ep.get('id') == entry['id']:
            ep.update({
                'file': entry['file'],
                'protocol': entry.get('protocol') or ep.get('protocol'),
                'description': entry.get('description', ep.get('description')),
                'aliases': entry.get('aliases', ep.get('aliases', [])),
                'required': entry.get('required', ep.get('required', False)),
            })
            return 'updated'
    # Otherwise append
    eps.append(entry)
    return 'added'


def ensure_competency_list(m: dict, competency_name: str):
    # Deprecated behavior kept for backward compatibility (no-op)
    # New behavior handled by ensure_entry_in_competencies
    return


def ensure_entry_in_competencies(m: dict, ep_id: str):
    """Ensure the entry point id is listed in top-level 'competencies'.
    If the array is missing, create it. If present, upsert the id.
    """
    if not ep_id:
        return
    comps = m.get('competencies')
    if not isinstance(comps, list):
        m['competencies'] = [ep_id]
        return
    if ep_id not in comps:
        comps.append(ep_id)


def main():
    p = argparse.ArgumentParser(description='Upsert an entry_point into a competency-manifest.json')
    p.add_argument('--competencies-dir', default=str(Path('olaf-core')/ 'competencies'), help='Root dir containing competencies')
    p.add_argument('--competency-id', required=True, help='Target competency folder name (e.g., prompt-engineer)')
    p.add_argument('--id', dest='ep_id', required=True, help='Entry point id (kebab-case)')
    p.add_argument('--file', required=True, help='Relative file path under the competency (e.g., prompts/foo.md)')
    p.add_argument('--protocol', default='Act', help='Protocol: Act | Propose-Act | Propose-Confirm-Act')
    p.add_argument('--description', default='', help='Short description')
    p.add_argument('--aliases', default='', help='Comma-separated aliases')
    p.add_argument('--required', action='store_true', help='Mark as required')
    p.add_argument('--competency-name', default='', help='Optional human-friendly competency name to add to list if present')
    args = p.parse_args()

    comp_dir = Path(args.competencies_dir) / args.competency_id
    manifest_path = comp_dir / 'competency-manifest.json'

    m = load_manifest(manifest_path)

    entry = {
        'id': args.ep_id,
        'file': args.file.replace('\\', '/'),
        'protocol': args.protocol,
        'description': args.description,
        'aliases': parse_aliases(args.aliases),
        'required': bool(args.required),
    }

    op = upsert_entry_point(m, entry)
    # Always mirror entry id into top-level competencies list
    ensure_entry_in_competencies(m, args.ep_id)

    save_manifest(manifest_path, m)
    print(f"Manifest {op}: {manifest_path} -> entry_point id={args.ep_id} file={entry['file']}")

if __name__ == '__main__':
    main()
