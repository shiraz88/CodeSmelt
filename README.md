python --version
   ```

2. Install the required dependency:
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

## Configuration

### Source File Extensions
The tool includes common source code file extensions by default (defined in `extensions.py`):
- Web: `.js`, `.ts`, `.jsx`, `.tsx`, `.vue`, `.svelte`, `.html`, `.css`, etc.
- Python: `.py`, `.pyi`, `.pyx`
- Java/Kotlin: `.java`, `.kt`, `.groovy`
- C-family: `.c`, `.cpp`, `.h`, `.hpp`
- And many more...

#### Customizing File Extensions
You can modify which file extensions are included by editing the `SOURCE_EXTENSIONS` set in `extensions.py`. For example, to include Unity3D script files while excluding other Unity files:

```python
SOURCE_EXTENSIONS = {
    # ... existing extensions ...

    # Unity3D specific
    '.cs',  # C# scripts
    '.shader', # Custom shaders
    '.asmdef', # Assembly definitions

    # ... other extensions ...
}
```

### Ignore Patterns
The tool automatically ignores files based on three levels:

1. Built-in patterns (`IGNORE_PATTERNS` in `extensions.py`):
   - Build outputs (`build/*`, `dist/*`, `*.pyc`, etc.)
   - Dependencies (`node_modules/*`, `vendor/*`, `venv/*`)
   - IDE files (`.idea/*`, `.vscode/*`)
   - Package lock files (`package-lock.json`, `poetry.lock`, etc.)
   - Binary and media files (`*.pdf`, `*.jpg`, `*.exe`, etc.)

2. Project's `.gitignore` rules (if present)
3. Directory-specific `.gitignore` rules

#### Customizing Ignore Patterns
To modify which files are ignored, you can:

1. Edit `IGNORE_PATTERNS` in `extensions.py`:
```python
IGNORE_PATTERNS = {
    # ... existing patterns ...

    # Unity3D specific ignores
    'Assets/AssetStoreTools/*',
    'Library/*',
    'Temp/*',
    'Logs/*',
    '*.unity',  # Unity scene files
    '*.meta',   # Unity meta files
    '*.prefab', # Unity prefab files

    # ... other patterns ...
}
```

2. Use your project's `.gitignore` file for project-specific exclusions

**Note**: Ignore patterns follow the same syntax as `.gitignore` files. The tool processes these rules in order:
1. Built-in `IGNORE_PATTERNS`
2. Project's root `.gitignore`
3. Directory-specific `.gitignore` files


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

## Troubleshooting

### Common Issues

1. **No Files Found**:
   - Verify the project path is correct
   - Check if files have supported extensions
   - Run with --debug to see which files are being filtered

2. **Missing Dependencies**:
   ```bash
   pip install --upgrade gitignore-parser