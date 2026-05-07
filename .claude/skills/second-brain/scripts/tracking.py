#!/usr/bin/env python3
"""
tracking.py - Raw file processing tracker for Second Brain.

Tracks which files in raw/ have been processed into wiki pages.
Unique identity: filename:sha256hash (directory is ignored).
If file content changes, the hash changes -> file needs reprocessing.
Old entries with stale hashes accumulate until 'clean' removes them.

Storage: .state.json in project root.
"""

import argparse
import hashlib
import json
import os
import sys
from datetime import date
from pathlib import Path

STATE_FILE = ".state.json"
RAW_DIR = "raw"
EXCLUDE_DIRS = {"assets"}


# --- Helpers ---

def find_root():
    """Find project root by locating raw/ directory."""
    for start in [Path(__file__).resolve().parent, Path.cwd()]:
        p = start
        while p != p.parent:
            if (p / RAW_DIR).is_dir():
                return p
            p = p.parent
    print("Error: no raw/ directory found.", file=sys.stderr)
    sys.exit(1)


def sha256(filepath):
    """SHA-256 hash of file content."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def make_key(filename, filehash):
    """Build unique key: filename:hash."""
    return f"{filename}:{filehash}"


def load_state(root):
    """Load state from .state.json."""
    p = root / STATE_FILE
    if p.exists():
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_state(root, state):
    """Save state to .state.json."""
    with open(root / STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def scan_raw(root):
    """Scan raw/ recursively (excluding assets/). Returns [(filename, relpath, fullpath)]."""
    raw = root / RAW_DIR
    result = []
    for dirpath, dirnames, filenames in os.walk(raw):
        rel = Path(dirpath).relative_to(raw)
        if rel.parts and rel.parts[0] in EXCLUDE_DIRS:
            continue
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fname in filenames:
            full = Path(dirpath) / fname
            relpath = str(full.relative_to(raw).as_posix())
            result.append((fname, relpath, full))
    return result


def resolve_path(root, filepath_arg):
    """Resolve a user-provided file path to (filename, relpath, fullpath)."""
    p = Path(filepath_arg)
    if not p.is_absolute():
        p = Path.cwd() / p
    p = p.resolve()
    if not p.exists():
        return None
    raw = (root / RAW_DIR).resolve()
    try:
        relpath = str(p.relative_to(raw).as_posix())
    except ValueError:
        relpath = p.name  # fallback if file is outside raw/
    return (p.name, relpath, p)


# --- Commands ---

def cmd_add(root, args):
    """Mark file(s) as processed. Computes hash and stores filename:hash key."""
    state = load_state(root)
    if not args.files:
        print("Usage: tracking.py add <file1> [file2] ...")
        return

    for filepath in args.files:
        resolved = resolve_path(root, filepath)
        if not resolved:
            print(f"  [!] Not found: {filepath}")
            continue
        filename, relpath, fullpath = resolved
        filehash = sha256(fullpath)
        key = make_key(filename, filehash)

        state[key] = {
            "path": relpath,
            "processed_at": str(date.today()),
        }
        print(f"  [+] {filename} (hash: {filehash[:12]}...)")

    save_state(root, state)


def cmd_next(root, args):
    """Show next N unprocessed files from raw/."""
    state = load_state(root)
    n = args.count or 10
    unprocessed = []

    for filename, relpath, fullpath in scan_raw(root):
        filehash = sha256(fullpath)
        key = make_key(filename, filehash)
        if key not in state:
            unprocessed.append((filename, relpath))

    if not unprocessed:
        print("All files are processed.")
        return

    count = min(n, len(unprocessed))
    print(f"Next {count} of {len(unprocessed)} unprocessed:\n")
    for filename, relpath in unprocessed[:count]:
        print(f"  raw/{relpath}")


def cmd_status(root, args):
    """Show overview of processed vs unprocessed files."""
    state = load_state(root)
    raw_files = scan_raw(root)

    processed = []
    unprocessed = []

    for filename, relpath, fullpath in raw_files:
        filehash = sha256(fullpath)
        key = make_key(filename, filehash)
        if key in state:
            processed.append((filename, relpath, state[key].get("processed_at", "?")))
        else:
            unprocessed.append((filename, relpath))

    total = len(raw_files)
    print(f"Total: {total} | Processed: {len(processed)} | Unprocessed: {len(unprocessed)}")
    print()

    if processed:
        print("--- Processed ---")
        for fname, relpath, pdate in processed:
            print(f"  [+] [{pdate}] {fname}")

    if unprocessed:
        print()
        print("--- Unprocessed ---")
        for fname, relpath in unprocessed:
            print(f"  [ ] raw/{relpath}")

    # stale entries in state
    current_keys = set()
    for filename, relpath, fullpath in raw_files:
        filehash = sha256(fullpath)
        current_keys.add(make_key(filename, filehash))
    stale = [k for k in state if k not in current_keys]
    if stale:
        print()
        print(f"--- Stale entries: {len(stale)} (run 'clean' to remove) ---")


def cmd_clean(root, args):
    """Remove stale entries: file deleted or hash changed."""
    state = load_state(root)
    raw_files = scan_raw(root)

    # Build set of current filename:hash keys
    current_keys = set()
    for filename, relpath, fullpath in raw_files:
        filehash = sha256(fullpath)
        current_keys.add(make_key(filename, filehash))

    stale = [k for k in state if k not in current_keys]
    if not stale:
        print("No stale entries. State is clean.")
        return

    for key in stale:
        del state[key]
        fname = key.rsplit(":", 1)[0]
        print(f"  [x] {fname} (stale hash)")

    save_state(root, state)
    print(f"\nRemoved {len(stale)} stale entries.")


def cmd_check(root, args):
    """Check if a specific file is processed (by current content hash)."""
    state = load_state(root)
    resolved = resolve_path(root, args.filename)

    if not resolved:
        # Try partial match against raw files
        raw_files = scan_raw(root)
        matches = [(fn, rp, fp) for fn, rp, fp in raw_files if args.filename.lower() in fn.lower()]
        if not matches:
            print(f"File not found: {args.filename}")
            return
        if len(matches) > 1:
            print(f"Multiple matches for '{args.filename}':")
            for fn, rp, _ in matches:
                print(f"  - raw/{rp}")
            return
        resolved = matches[0]

    filename, relpath, fullpath = resolved
    filehash = sha256(fullpath)
    key = make_key(filename, filehash)

    if key in state:
        pdate = state[key].get("processed_at", "?")
        print(f"  [+] {filename}: PROCESSED ({pdate})")
    else:
        print(f"  [ ] {filename}: UNPROCESSED")
    print(f"      Path: raw/{relpath}")
    print(f"      Hash: {filehash[:16]}...")


def cmd_help(root, args):
    """Show help with all commands."""
    print("""tracking.py - Raw file processing tracker for Second Brain
==========================================================

Tracks which files in raw/ have been processed.
Unique key: filename:sha256 (directory ignored).
If content changes, hash changes -> needs reprocessing.

Storage: .state.json (project root)

Commands:
  add <file> [...]   Mark file(s) as processed
  next [N]           Show next N unprocessed files (default: 5)
  status             Overview: processed vs unprocessed
  clean              Remove stale entries (deleted/changed files)
  check <file>       Check if a specific file is processed
  help               This message

Examples:
  tracking.py add raw/pages/article.md
  tracking.py add raw/pages/part1.md raw/pages/part2.md
  tracking.py next 3
  tracking.py status
  tracking.py check "Config Flow"
  tracking.py clean

AI agent workflow:
  1. Agent runs: tracking.py next 3
  2. Agent processes returned files via /second-brain-ingest
  3. Agent runs: tracking.py add <processed-file>
  4. Repeat
""")


# --- Main ---

def main():
    parser = argparse.ArgumentParser(
        description="Raw file processing tracker", add_help=False
    )
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="Mark file(s) as processed")
    p_add.add_argument("files", nargs="*", help="File path(s) to mark")

    p_next = sub.add_parser("next", help="Next N unprocessed files")
    p_next.add_argument("count", nargs="?", type=int, default=5)

    sub.add_parser("status", help="Show processed/unprocessed overview")
    sub.add_parser("clean", help="Remove stale entries")

    p_check = sub.add_parser("check", help="Check specific file")
    p_check.add_argument("filename", help="File path or partial name")

    sub.add_parser("help", help="Show detailed help")

    args = parser.parse_args()
    root = find_root()

    cmds = {
        "add": cmd_add, "next": cmd_next, "status": cmd_status,
        "clean": cmd_clean, "check": cmd_check, "help": cmd_help,
    }

    if not args.command or args.command == "help":
        cmd_help(root, args)
    else:
        cmds[args.command](root, args)


if __name__ == "__main__":
    main()
