# CodeSmelt: Source Code Concatenator

![CodeSmelt Logo](assets/CodeSmeltLogo.jpg)

**CodeSmelt** is a command-line tool that “melts down” your Git project’s source code into a single, well-organized file. It not only concatenates source files but also embeds a tree-like directory structure (unless omitted) to help you quickly understand your project’s layout. This is especially useful for code analysis, preparing inputs for language models, or sharing project snapshots.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Custom Output & Debug Mode](#custom-output--debug-mode)
- [Configuration](#configuration)
  - [Source File Extensions](#source-file-extensions)
  - [Ignore Patterns](#ignore-patterns)
- [Tips for Using with LLMs](#tips-for-using-with-llms)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Features

- **Concatenation with Context:** Combines all source files (with supported extensions by default) into one file while preserving directory hierarchy.
- **Smart Filtering:** Uses built-in file extension whitelists and ignore patterns. Also honors your project’s `.gitignore` for extra filtering.
- **Encoding Handling:** Automatically handles file encoding issues (tries UTF-8 first, then falls back to Latin-1).
- **Debug Logging:** Option to enable debug logging so you can see which files are being included or skipped.
- **Customizable Output:** Optionally omit the directory structure and disable file extension filtering via command-line flags.
- **Easy Customization:** Adjust supported file extensions and ignore patterns via the `extensions.py` file.

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/codesmelt.git
   cd codesmelt
   ```

2. **Install Dependencies:**

   CodeSmelt requires Python 3. Install all required packages using the `requirements.txt` file:

   ```bash
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

### Custom Output, Debug Mode, and New Options

- **Specify a Custom Output File:**

  ```bash
  python codesmelt.py -o output.txt /path/to/project
  ```

- **Enable Debug Logging:**

  ```bash
  python codesmelt.py -d -o output.txt /path/to/project
  ```

- **Omit the Directory Structure from the Output:**

  ```bash
  python codesmelt.py -n /path/to/project
  ```

- **Disable File Extension Filtering (Include All Files):**

  ```bash
  python codesmelt.py -e /path/to/project
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
   - Ensure your project contains files with supported extensions (unless using `-e` to disable filtering).
   - Run with `--debug` to see detailed file filtering information.

2. **Missing Dependencies:**
   - Make sure you have installed all required packages by running:
     
     ```bash
     pip install -r requirements.txt
     ```

3. **Permission Issues:**
   - Make sure you have read permissions for the project directory and write permissions for the output file.

---

## Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or additional features, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the [MIT License](LICENSE). *(Replace with your actual license if different.)*

---

## Author

**Shiraz Akmal**

Feel free to reach out if you have any questions or feedback!

---

Happy coding with CodeSmelt!
