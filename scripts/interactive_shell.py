#!/usr/bin/env python3
"""
Interactive CLI Explorer for The Modern Azure Enterprise Cheat Sheet & Architecture Handbook:
Search, inspect, and explore 300+ Azure services, architectures, runbooks, cheatsheets, and interview guides.

Usage:
    python scripts/interactive_shell.py "private endpoint"
    python scripts/interactive_shell.py --cheatsheets
    python scripts/interactive_shell.py --architectures
    python scripts/interactive_shell.py --runbooks
    python scripts/interactive_shell.py --interview
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CHEATSHEETS_DIR = BASE_DIR / "cheatsheets"
RUNBOOKS_DIR = BASE_DIR / "runbooks"
ARCH_DIR = BASE_DIR / "architectures"
INTERVIEW_DIR = BASE_DIR / "interview"

def list_cheatsheets():
    print("\n📚 Azure Enterprise Cheatsheets & Fast References\n" + "=" * 80)
    for cs in sorted(list(CHEATSHEETS_DIR.glob("*.md"))):
        print(f"   ⚡ {cs.name}")
    print("\n" + "=" * 80)

def list_runbooks():
    print("\n🚨 Azure Production Incident Runbooks\n" + "=" * 80)
    for rb in sorted(list(RUNBOOKS_DIR.glob("*.md"))):
        print(f"   🚨 {rb.name}")
    print("\n" + "=" * 80)

def list_architectures():
    print("\n🏛️ Azure Enterprise Production Architecture Blueprints\n" + "=" * 80)
    for arch in sorted(list(ARCH_DIR.glob("*.md"))):
        print(f"   🏛️ {arch.name}")
    print("\n" + "=" * 80)

def list_interviews():
    print("\n🎓 Azure 4-Tier Interview Preparation Matrix & Flashcards\n" + "=" * 80)
    for iv in sorted(list(INTERVIEW_DIR.glob("*.md"))):
        print(f"   🎓 {iv.name}")
    print("\n" + "=" * 80)

def find_file(query: str):
    clean_q = query.lower().replace(" ", "-")
    clean_q_us = query.lower().replace(" ", "_")
    
    # Substring search in filenames across all dirs
    for search_dir in [CHEATSHEETS_DIR, RUNBOOKS_DIR, ARCH_DIR, INTERVIEW_DIR]:
        matches = list(search_dir.glob(f"*{clean_q}*.md")) or list(search_dir.glob(f"*{clean_q_us}*.md"))
        if matches:
            return matches[0]
        
    # Search content in files
    for search_dir in [CHEATSHEETS_DIR, RUNBOOKS_DIR, ARCH_DIR, INTERVIEW_DIR]:
        for doc in sorted(list(search_dir.glob("*.md"))):
            if query.lower() in doc.read_text(encoding="utf-8").lower():
                return doc
            
    return None

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python scripts/interactive_shell.py <keyword_or_topic>")
        print("       python scripts/interactive_shell.py --cheatsheets")
        print("       python scripts/interactive_shell.py --runbooks")
        print("       python scripts/interactive_shell.py --architectures")
        print("       python scripts/interactive_shell.py --interview")
        print("Example: python scripts/interactive_shell.py 'private endpoint'")
        print("         python scripts/interactive_shell.py bicep")
        sys.exit(0)

    arg = sys.argv[1]
    if arg == "--cheatsheets":
        list_cheatsheets()
        sys.exit(0)
    elif arg == "--runbooks":
        list_runbooks()
        sys.exit(0)
    elif arg == "--architectures":
        list_architectures()
        sys.exit(0)
    elif arg == "--interview":
        list_interviews()
        sys.exit(0)

    match = find_file(arg)
    if not match:
        print(f"❌ No matching cheatsheet, runbook, architecture, or interview topic found for: '{arg}'")
        sys.exit(1)

    print(f"\n📖 Found: {match.name}\n" + "=" * 80)
    print(match.read_text(encoding="utf-8"))
    print("=" * 80)

if __name__ == "__main__":
    main()
