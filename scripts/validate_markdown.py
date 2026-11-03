#!/usr/bin/env python3
"""
validate_markdown.py
Repository Integrity & Relative Link Verification Suite for azure-cheat-sheet
"""

import os
import re
import sys

def find_markdown_files(repo_root):
    md_files = []
    for root, dirs, files in os.walk(repo_root):
        if ".git" in dirs:
            dirs.remove(".git")
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    return sorted(md_files)

def check_relative_links(repo_root, md_files):
    # Regex to find markdown links: [text](path)
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    errors = []

    for file_path in md_files:
        rel_path = os.path.relpath(file_path, repo_root)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            errors.append(f"Encoding Error in {rel_path}: {e}")
            continue

        file_dir = os.path.dirname(file_path)
        for match in link_pattern.finditer(content):
            target = match.group(2).strip()

            # Skip web URLs, email links, anchor-only links, KaTeX math expressions, and images
            if target.startswith(("http://", "https://", "mailto:", "#", "javascript:")):
                continue

            # Strip anchor if present (e.g. "./file.md#section" -> "./file.md")
            target_file = target.split("#")[0]
            if not target_file:
                continue

            target_path = os.path.normpath(os.path.join(file_dir, target_file))
            if not os.path.exists(target_path):
                errors.append(f"Broken relative link in {rel_path} -> '{target}' (resolved to: {os.path.relpath(target_path, repo_root)})")

    return errors

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(f"🔍 Scanning Markdown files in {repo_root}...")

    md_files = find_markdown_files(repo_root)
    print(f"Found {len(md_files)} markdown files.")

    errors = check_relative_links(repo_root, md_files)

    if errors:
        print("\n❌ Validation Failed! Errors detected:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("\n✅ All Markdown files and relative links verified successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
