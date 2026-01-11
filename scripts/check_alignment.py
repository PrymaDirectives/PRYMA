#!/usr/bin/env python3
"""
PRYMA Framework Alignment Checker

Validates repository content against framework.md canonical definitions.
Scans for outdated terminology, missing archetypes, and inconsistent references.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Canonical archetypes from framework.md
CANONICAL_ARCHETYPES = {
    "Lumen": "The Oracle (reasoning core)",
    "Strike": "The Warrior (execution engine)",
    "Echo": "The Herald (communications hub)",
    "Sentinel": "The Guardian (security guardian)",
    "Argus": "The All-Seeing Guardian (perception/monitoring)",
    "Sage": "The Architect (planning/strategy)",
    "Archive": "The Librarian (knowledge/memory)",
    "Spirit": "The Swarm (micro-agents)",
    "Shade": "The Trickster (adversarial sandbox)"
}

# Deprecated/outdated terms to flag
DEPRECATED_TERMS = [
    r"\bObserver\b(?!\s+pattern)",  # "Observer" except when referring to design pattern
    r"\bWatcher\b(?!\s+log)",  # "Watcher" except in "log watcher"
    r"\bMonitor\s+Agent\b",  # "Monitor Agent" (should be Argus or Sentinel)
    r"\bagent\s+types\b(?!\.md)",  # Prefer "archetypes" or "container types"
]

# Required terminology (should appear in key docs)
REQUIRED_PHRASES = [
    "container-first",
    "cryptographically governed",
    "autonomic",
    "Solana governance",
]

# Files to check (relative to repo root)
CHECK_PATTERNS = [
    "**/*.md",
    "**/*.yaml",
    "**/*.yml",
    "**/README*",
]

# Exclude patterns
EXCLUDE_PATTERNS = [
    "**/node_modules/**",
    "**/book/**",
    "**/gh-pages-worktree/**",
    "**/.git/**",
    "**/bak/**",
]


class AlignmentChecker:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.errors: List[Dict] = []
        self.warnings: List[Dict] = []
        self.framework_path = repo_root / "framework.md"
        
    def check_file(self, file_path: Path) -> None:
        """Check a single file for alignment issues."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            rel_path = file_path.relative_to(self.repo_root)
            
            # Check for deprecated terms
            for pattern in DEPRECATED_TERMS:
                matches = re.finditer(pattern, content, re.IGNORECASE)
                for match in matches:
                    line_num = content[:match.start()].count('\n') + 1
                    self.warnings.append({
                        'file': str(rel_path),
                        'line': line_num,
                        'type': 'deprecated_term',
                        'text': match.group(0),
                        'message': f'Deprecated term "{match.group(0)}" found'
                    })
            
            # Check archetype references
            self._check_archetypes(content, rel_path)
            
        except Exception as e:
            self.errors.append({
                'file': str(file_path.relative_to(self.repo_root)),
                'type': 'read_error',
                'message': str(e)
            })
    
    def _check_archetypes(self, content: str, rel_path: Path) -> None:
        """Verify archetype names and descriptions match framework."""
        # Look for archetype lists
        archetype_list_pattern = r'(?:Archetypes?|Agent Types?|Container Types?):\s*\n((?:\s*[-*]\s+\*\*\w+\*\*.*\n?)+)'
        matches = re.finditer(archetype_list_pattern, content, re.IGNORECASE)
        
        for match in matches:
            list_content = match.group(1)
            found_archetypes = set(re.findall(r'\*\*(\w+)\*\*', list_content))
            expected_archetypes = set(CANONICAL_ARCHETYPES.keys())
            
            missing = expected_archetypes - found_archetypes
            if missing and "Argus" in missing:
                line_num = content[:match.start()].count('\n') + 1
                self.warnings.append({
                    'file': str(rel_path),
                    'line': line_num,
                    'type': 'missing_archetype',
                    'text': f'Missing archetypes: {", ".join(sorted(missing))}',
                    'message': 'Archetype list incomplete compared to framework.md'
                })
    
    def scan_directory(self, directory: Path = None) -> None:
        """Recursively scan directory for files to check."""
        if directory is None:
            directory = self.repo_root
            
        for pattern in CHECK_PATTERNS:
            for file_path in directory.glob(pattern):
                # Skip excluded paths
                if any(file_path.match(excl) for excl in EXCLUDE_PATTERNS):
                    continue
                    
                if file_path.is_file():
                    self.check_file(file_path)
    
    def check_framework_references(self) -> None:
        """Ensure key documents reference framework.md."""
        key_docs = [
            self.repo_root / "README.md",
            self.repo_root / "docs" / "README.md",
            self.repo_root / "docs" / "whitepaper" / "README.md",
        ]
        
        for doc in key_docs:
            if not doc.exists():
                continue
                
            with open(doc, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if "framework.md" not in content:
                self.warnings.append({
                    'file': str(doc.relative_to(self.repo_root)),
                    'type': 'missing_framework_ref',
                    'message': 'Key document does not reference framework.md'
                })
    
    def report(self) -> int:
        """Print report and return exit code."""
        print("=" * 70)
        print("PRYMA Framework Alignment Check")
        print("=" * 70)
        print()
        
        if self.errors:
            print(f"❌ ERRORS: {len(self.errors)}")
            for err in self.errors:
                print(f"  {err['file']}: {err['message']}")
            print()
        
        if self.warnings:
            print(f"⚠️  WARNINGS: {len(self.warnings)}")
            for warn in self.warnings[:20]:  # Limit output
                loc = f"{warn['file']}:{warn.get('line', '?')}"
                print(f"  {loc}: {warn['message']}")
                if 'text' in warn:
                    print(f"    → {warn['text']}")
            
            if len(self.warnings) > 20:
                print(f"  ... and {len(self.warnings) - 20} more warnings")
            print()
        
        if not self.errors and not self.warnings:
            print("✅ All checks passed! Repository is aligned with framework.md")
            print()
            return 0
        
        print(f"Total: {len(self.errors)} errors, {len(self.warnings)} warnings")
        print()
        print("See framework.md for canonical definitions.")
        return 1 if self.errors else 0


def main():
    repo_root = Path(__file__).parent.parent
    checker = AlignmentChecker(repo_root)
    
    print(f"Scanning repository: {repo_root}")
    print(f"Framework reference: {checker.framework_path}")
    print()
    
    checker.scan_directory()
    checker.check_framework_references()
    
    exit_code = checker.report()
    exit(exit_code)


if __name__ == "__main__":
    main()
