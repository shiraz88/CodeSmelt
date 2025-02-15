pip install -r requirements.txt
   ```

   *(If you use a virtual environment, activate it before installing.)*

3. **Ensure File Structure:**

   Make sure the following files are in the same directory:

   - `codesmelt.py`
   - `extensions.py`
   - `README.md`
   - `requirements.txt`
   - `assets/CodeSmeltLogo.jpg` (logo image)

---

## Usage

### Basic Usage

Run CodeSmelt by providing the path to your Git project. For example:

```bash
python codesmelt.py /path/to/project
```

### Custom Output & Debug Mode

- **Specify a Custom Output File:**

  ```bash
  python codesmelt.py -o output.txt /path/to/project
  ```

- **Enable Debug Logging:**

  ```bash
  python codesmelt.py -d -o output.txt /path/to/project
  ```

- **Omit Directory Structure:**

  ```bash
  python codesmelt.py -n -o output.txt /path/to/project
  ```

#### Command-line Arguments

- `project_path` (required): Path to your Git project directory.
- `-o, --output`: Specify the output file path (default: `concatenated_source.txt`).
- `-d, --debug`: Enable debug logging to get detailed information about file selection.
- `-n, --no-structure`: Omit the directory structure from the output file.
- `-e, --no-extensions`: Disable file extension filtering (include all files regardless of extension).


---

## Configuration

CodeSmelt uses the `extensions.py` file to define:

### Source File Extensions

The tool automatically includes many common source code file extensions. Examples include:

- **Web:** `.js`, `.ts`, `.jsx`, `.tsx`, `.vue`, `.svelte`, `.html`, `.css`, etc.
- **Python:** `.py`, `.pyi`, `.pyx`
- **Java/Kotlin:** `.java`, `.kt`, `.groovy`
- **C-family:** `.c`, `.cpp`, `.h`, `.hpp`
- **Other Languages:** Ruby (`.rb`), PHP (`.php`), Go (`.go`), Rust (`.rs`), Swift (`.swift`), Shell (`.sh`), and more.

*To add or remove extensions, edit the `SOURCE_EXTENSIONS` set in `extensions.py`.*

### Ignore Patterns

Files and directories are automatically ignored based on three levels:

1. **Built-in Patterns:** Defined in the `IGNORE_PATTERNS` set in `extensions.py` (e.g., build outputs, dependency directories, IDE files, binary/media files).
2. **Project’s `.gitignore`:** If a `.gitignore` is present at the root of your project, CodeSmelt honors its rules.
3. **Directory-specific Rules:** Additional `.gitignore` files in subdirectories will also be considered.

*To customize, modify the `IGNORE_PATTERNS` in `extensions.py`.*

Example of adding Unity3D-specific ignores:

```python
IGNORE_PATTERNS = {
    # ... existing patterns ...
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

---

## Tips for Using with LLMs

1. **Token Management:**
   - For very large projects, consider concatenating only specific directories to avoid token limits.
   - Use debug mode (`-d`) to verify which files are included/excluded.

2. **Effective Prompting:**
   - Reference files using their relative paths as shown in the generated directory structure.
   - Ask questions about specific sections of the output using the file headers.

3. **Best Practices:**
   - Always review the concatenated output before sending it to an LLM.
   - For large projects, consider breaking down the analysis into smaller, manageable components.

---

## Troubleshooting

### Common Issues

1. **No Files Found:**
   - Double-check the project path.
   - Ensure your project contains files with supported extensions.
   - Run with `--debug` to see detailed file filtering information.

2. **Missing Dependencies:**
   - Make sure you have installed all required packages by running:

     ```bash
     pip install -r requirements.txt