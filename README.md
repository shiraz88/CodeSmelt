# CodeSmelt: Source Code Concatenator

![CodeSmelt Logo](assets/CodeSmeltLogo.jpg)

**CodeSmelt** is a command-line tool that melts down your Git project’s source code into a single, well-organized file. It concatenates all source files (with supported extensions by default) and can optionally include a visual, tree-like directory structure to showcase your project's organization. In addition, CodeSmelt supports AI-generated documentation summaries using various LLM providers.

**Author:** Shiraz Akmal & AI

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Custom Output & Debug Mode](#custom-output--debug-mode)
  - [AI Summary Generation](#ai-summary-generation)
- [Configuration](#configuration)
  - [Source File Extensions](#source-file-extensions)
  - [Ignore Patterns](#ignore-patterns)
- [Environment Variables](#environment-variables)
- [Tips for Using with LLMs](#tips-for-using-with-llms)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Features

- **Source Code Concatenation:** Combine all source files into a single file with a header that includes the generation timestamp and project path.
- **Directory Structure Inclusion:** Optionally include a visual, tree-like directory structure to understand your project’s organization.
- **File Filtering:** Uses smart filtering based on file extensions and ignore patterns (modifiable via `extensions.py`). You can disable file extension filtering with a command-line flag.
- **Debug Logging:** Enable detailed logging to see which files are being processed and why some may be skipped.
- **AI Documentation Summary:** Generate an AI-powered documentation summary using your choice of LLM providers.
- **Customizable AI Model:** Specify a custom AI model for summary generation using the `-m/--model` flag (supports models like `gpt-4`, `gpt-3.5-turbo`, `grok-2-1212`, and `grok-2-vision-1212`).

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
   - `ai_integration.py`
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

  *(You can also provide the output file as the second positional argument.)*

- **Enable Debug Logging:**

  ```bash
  python codesmelt.py -d /path/to/project
  ```

- **Omit Directory Structure:**

  ```bash
  python codesmelt.py -n /path/to/project
  ```

- **Disable File Extension Filtering (Include All Files):**

  ```bash
  python codesmelt.py -e /path/to/project
  ```

### AI Summary Generation

- **Generate AI Documentation Summary:**

  ```bash
  python codesmelt.py -s /path/to/project
  ```

- **Use a Custom AI Model:**

  ```bash
  # Using OpenAI models:
  python codesmelt.py -s -m gpt-4 /path/to/project
  python codesmelt.py -s -m gpt-3.5-turbo /path/to/project

  # Using xAI models:
  python codesmelt.py -s -m grok-2-1212 /path/to/project
  python codesmelt.py -s -m grok-2-vision-1212 /path/to/project
  ```

#### Command-line Arguments

- **project_path (required):** Path to your Git project directory.
- **-o, --output:** Specify the output file path (default: `concatenated_source.txt`).
- **-d, --debug:** Enable debug logging.
- **-n, --no-structure:** Omit the directory structure from the output.
- **-e, --no-extensions:** Disable file extension filtering (include all files regardless of extension).
- **-s, --summary:** Generate an AI documentation summary (requires API keys).
- **-m, --model:** Specify a custom AI model for summary generation. Examples:
  - OpenAI: `gpt-4`, `gpt-3.5-turbo`
  - xAI: `grok-2-1212`, `grok-2-vision-1212`

---

## Configuration

### Source File Extensions

The tool automatically includes many common source code file extensions. Examples include:

- **Web:** `.js`, `.ts`, `.jsx`, `.tsx`, `.vue`, `.svelte`, `.html`, `.css`, etc.
- **Python:** `.py`, `.pyi`, `.pyx`
- **Java/Kotlin:** `.java`, `.kt`, `.groovy`
- **C-family:** `.c`, `.cpp`, `.h`, `.hpp`
- **Other Languages:** Ruby (`.rb`), PHP (`.php`), Go (`.go`), Rust (`.rs`), Swift (`.swift`), Shell (`.sh`), etc.

*To add or remove extensions, edit the `SOURCE_EXTENSIONS` set in `extensions.py`.*

### Ignore Patterns

Files and directories are automatically ignored based on:

1. **Built-in Patterns:** Defined in the `IGNORE_PATTERNS` set in `extensions.py` (e.g., build outputs, dependency directories, IDE files, binary/media files).
2. **Project’s `.gitignore`:** CodeSmelt honors the rules in your project's `.gitignore`.
3. **Directory-specific Rules:** Additional `.gitignore` files in subdirectories are also considered.

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

## Environment Variables

For AI summary generation, ensure you have set the appropriate API keys:

- **OpenAI:** Set the `OPENAI_API_KEY` environment variable.
- **xAI:** Set the `XAI_API_KEY` environment variable.

These keys are required to generate documentation summaries using AI.

---

## Tips for Using with LLMs

1. **Token Management:**
   - For very large projects, consider concatenating only specific directories to avoid exceeding token limits.
   - Use debug mode (`-d`) to verify file inclusion/exclusion.

2. **Effective Prompting:**
   - Reference files using their relative paths as shown in the generated directory structure.
   - Ask questions about specific sections of the output using file headers.

3. **Best Practices:**
   - Always review the concatenated output before sending it to an LLM.
   - For large projects, consider breaking down the analysis into smaller, manageable parts.

---

## Troubleshooting

### Common Issues

1. **No Files Found:**
   - Verify that the project path is correct.
   - Ensure your project contains files with supported extensions (unless using `-e`).
   - Run with `--debug` to see detailed file filtering information.

2. **Missing Dependencies:**
   - Install required packages by running:
     ```bash
     pip install -r requirements.txt
     ```

3. **API Key Issues (for AI Summary):**
   - Ensure the appropriate API keys (`OPENAI_API_KEY` or `XAI_API_KEY`) are set.
   - If a summary is not generated, check for token limits or API errors in the debug output.

4. **Permission Issues:**
   - Ensure you have read permissions for the project directory and write permissions for the output file.

---

## Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or additional features, please fork the repository and submit a pull request. For major changes, open an issue first to discuss your proposed changes.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

**Shiraz Akmal**

Feel free to reach out (https://x.com/shirazakmal) if you have any questions or feedback!

---

Happy coding with CodeSmelt!
