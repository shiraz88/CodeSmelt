#!/usr/bin/env python3
"""
CodeSmelt: Source Code Concatenator

This tool melts down source code files from a git project into a single file,
including directory structure information.
"""

import argparse
import sys
from pathlib import Path
import os
from typing import Set, List, Optional
import fnmatch
from datetime import datetime
import gitignore_parser
from extensions import SOURCE_EXTENSIONS, IGNORE_PATTERNS

class CodeSmelt:
    def __init__(self, project_path: str, output_file: str):
        self.project_path = Path(project_path).resolve()
        self.output_file = Path(output_file)
        self.gitignore_matcher = self._setup_gitignore()
        self.debug = False
        self.include_structure = True
        self.include_extensions = True  # New flag for controlling extension filtering

    def _setup_gitignore(self) -> Optional[callable]:
        """Setup gitignore matcher if .gitignore exists"""
        gitignore_path = self.project_path / '.gitignore'
        if gitignore_path.exists():
            try:
                return gitignore_parser.parse_gitignore(gitignore_path)
            except Exception as e:
                print(f"Warning: Failed to parse .gitignore: {e}")
        return None

    def _should_include_file(self, file_path: Path) -> bool:
        """Check if file should be included based on extension and ignore rules"""
        # Skip common virtual environment and system directories
        excluded_dirs = {
            '.git', '__pycache__', '.pythonlibs', 'venv', 'node_modules',
            '.cache', '.local', '.upm', '.config', '.npm', '.nix-profile',
            'dist', 'build', 'target'
        }

        try:
            # Convert to relative path for checking
            try:
                rel_path = file_path.relative_to(self.project_path)
            except ValueError:
                if self.debug:
                    print(f"Debug: Skipping file outside project path: {file_path}")
                return False

            # Check for excluded directories in the path
            if any(part in excluded_dirs for part in file_path.parts):
                if self.debug:
                    print(f"Debug: Skipping excluded directory: {file_path}")
                return False

            # Check file extension only if extension filtering is enabled
            if self.include_extensions and file_path.suffix.lower() not in SOURCE_EXTENSIONS:
                if self.debug:
                    print(f"Debug: Skipping non-source file: {file_path}")
                return False

            # Check custom ignore patterns
            for pattern in IGNORE_PATTERNS:
                if fnmatch.fnmatch(str(rel_path), pattern):
                    if self.debug:
                        print(f"Debug: Skipping ignored pattern {pattern}: {file_path}")
                    return False

            # Check .gitignore if available
            if self.gitignore_matcher:
                try:
                    should_include = not self.gitignore_matcher(str(file_path))
                    if self.debug and not should_include:
                        print(f"Debug: Skipping gitignored file: {file_path}")
                    return should_include
                except Exception as e:
                    print(f"Warning: gitignore matching failed for {file_path}: {e}")
                    return True

            if self.debug:
                print(f"Debug: Including file: {file_path}")
            return True

        except Exception as e:
            print(f"Warning: Error checking file {file_path}: {e}")
            return False

    def _get_file_content(self, file_path: Path) -> str:
        """Read file content with proper encoding handling"""
        try:
            # Try UTF-8 first
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            try:
                # Fallback to latin-1
                with open(file_path, 'r', encoding='latin-1') as f:
                    return f.read()
            except Exception as e:
                print(f"Warning: Failed to read {file_path}: {e}")
                return f"ERROR: Could not read file {file_path}\n"

    def _generate_directory_structure(self) -> str:
        """Generate a tree-like directory structure"""
        structure = ["Directory Structure:", ""]

        def add_to_tree(path: Path, prefix: str = ""):
            # Skip excluded directories
            excluded_dirs = {
                '.git', '__pycache__', '.pythonlibs', 'venv', 'node_modules',
                '.cache', '.local', '.upm', '.config', '.npm', '.nix-profile',
                'dist', 'build', 'target'
            }
            if path.name in excluded_dirs:
                return

            # Add files first
            files = sorted([p for p in path.iterdir() if p.is_file()])
            included_files = [f for f in files if self._should_include_file(f)]

            for idx, file in enumerate(included_files):
                is_last = idx == len(included_files) - 1
                structure.append(f"{prefix}{'└──' if is_last else '├──'} {file.name}")

            # Then add directories
            dirs = sorted([p for p in path.iterdir() if p.is_dir()])
            included_dirs = [d for d in dirs if d.name not in excluded_dirs]

            for idx, dir in enumerate(included_dirs):
                is_last = idx == len(included_dirs) - 1
                structure.append(f"{prefix}{'└──' if is_last else '├──'} {dir.name}/")
                add_to_tree(dir, prefix + ("    " if is_last else "│   "))

        add_to_tree(self.project_path)
        return "\n".join(structure)

    def concatenate(self, debug: bool = False):
        """Main method to concatenate all source files"""
        self.debug = debug
        if not self.project_path.exists():
            print(f"Error: Project path {self.project_path} does not exist")
            return False

        try:
            with open(self.output_file, 'w', encoding='utf-8') as out:
                # Write header
                header = f"""
# Project Source Code Concatenation
# Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Project path: {self.project_path}

"""
                out.write(header)

                # Write directory structure if enabled
                if self.include_structure:
                    out.write(self._generate_directory_structure())
                    out.write("\n\n" + "="*80 + "\n\n")

                # Process all files
                file_count = 0
                for file_path in self.project_path.rglob('*'):
                    if file_path.is_file() and self._should_include_file(file_path):
                        rel_path = file_path.relative_to(self.project_path)

                        # Write file header
                        out.write(f"\n\n# File: {rel_path}\n")
                        out.write("="*80 + "\n\n")

                        # Write file content
                        content = self._get_file_content(file_path)
                        out.write(content)
                        file_count += 1

                print(f"Successfully melted {file_count} files to {self.output_file}")
                return True

        except Exception as e:
            print(f"Error during melting: {e}")
            return False

def main():
    parser = argparse.ArgumentParser(
        description="CodeSmelt: Melt down your git project's source code into a single file",
        usage="%(prog)s project_path [output_file] [-o OUTPUT] [-d] [-n] [-e]"
    )

    # Add the project path as required positional argument
    parser.add_argument(
        "project_path",
        help="Path to the git project directory"
    )

    # Add optional positional argument for output file
    parser.add_argument(
        "output_file",
        nargs="?",  # Make it optional
        help="Output file path (alternative to -o)",
        default=None
    )

    # Keep the original -o option for backward compatibility
    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: concatenated_source.txt)",
        default=None
    )

    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="Enable debug logging"
    )

    parser.add_argument(
        "-n", "--no-structure",
        action="store_true",
        help="Omit directory structure from output"
    )

    parser.add_argument(
        "-e", "--no-extensions",
        action="store_true",
        help="Disable file extension filtering"
    )

    args = parser.parse_args()

    # Determine the output file path, prioritizing command line arguments
    output_file = args.output or args.output_file or "concatenated_source.txt"

    concatenator = CodeSmelt(args.project_path, output_file)
    concatenator.include_structure = not args.no_structure
    concatenator.include_extensions = not args.no_extensions
    success = concatenator.concatenate(debug=args.debug)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()