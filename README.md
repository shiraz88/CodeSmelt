git clone https://github.com/yourusername/codesmelt.git
   cd codesmelt
   ```

2. Ensure you have Python 3.11 or later installed:
   ```bash
   python --version
   ```

3. Install the required dependency:
   ```bash
   pip install gitignore-parser
   ```

## Usage

Basic usage:
```bash
python codesmelt.py /path/to/project -o output.txt
```

With debug logging:
```bash
python codesmelt.py /path/to/project -o output.txt --debug
```

### Command-line Arguments

- `project_path`: Path to the Git project directory (required)
- `-o, --output`: Output file path (default: concatenated_source.txt)
- `-d, --debug`: Enable debug logging

## Tips for Using with LLMs

1. **Token Management**:
   - For large projects, consider concatenating only specific directories
   - Use the debug mode to see which files are included/excluded
   - Remove unnecessary documentation files if you're close to token limits

2. **Effective Prompting**:
   - Reference files using their relative paths as shown in the directory structure
   - Use the directory structure to ask about specific components
   - Refer to file relationships based on the visual structure

3. **Best Practices**:
   - Review the concatenated output before sending to ensure relevance
   - For large projects, break down analysis into smaller, focused components
   - Use the debug mode to verify file selection when customizing

## Output Format

The generated file includes:
1. A timestamp and project path header
2. A visual directory structure of the project
3. The contents of each source file, clearly separated with headers

Example output:
```
# Project Source Code Concatenation
# Generated on: 2025-02-15 20:53:29
# Project path: /path/to/project

Directory Structure:
├── src/
│   ├── main.py
│   └── utils.py
└── README.md

================================================================================

# File: src/main.py
================================================================================
[File contents here]

# File: src/utils.py
================================================================================
[File contents here]
```

## Configuration

### Source File Extensions
The tool includes common source code file extensions by default (defined in `extensions.py`):
- Web: `.js`, `.ts`, `.jsx`, `.tsx`, `.vue`, `.svelte`, `.html`, `.css`, etc.
- Python: `.py`, `.pyi`, `.pyx`
- Java/Kotlin: `.java`, `.kt`, `.groovy`
- C-family: `.c`, `.cpp`, `.h`, `.hpp`
- And many more...

### Ignore Patterns
The tool automatically ignores:
- Build outputs (`build/*`, `dist/*`, `*.pyc`, etc.)
- Dependencies (`node_modules/*`, `vendor/*`, `venv/*`)
- IDE files (`.idea/*`, `.vscode/*`)
- Package lock files (`package-lock.json`, `poetry.lock`, etc.)
- Binary and media files (`*.pdf`, `*.jpg`, `*.exe`, etc.)

## Troubleshooting

### Common Issues

1. **No Files Found**:
   - Verify the project path is correct
   - Check if files have supported extensions
   - Run with --debug to see which files are being filtered

2. **Missing Dependencies**:
   ```bash
   pip install --upgrade gitignore-parser