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

### Custom Output & Debug Mode

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

### AI Summary Generation

- **Generate Basic Documentation Summary:**

  Uses the default AI model to generate documentation:
  ```bash
  python codesmelt.py -s /path/to/project
  ```

- **Use Custom AI Model:**

  Choose specific models for summary generation:
  ```bash
  # Using OpenAI models
  python codesmelt.py -s -m gpt-4 /path/to/project
  python codesmelt.py -s -m gpt-3.5-turbo /path/to/project

  # Using xAI models
  python codesmelt.py -s -m grok-2-1212 /path/to/project
  python codesmelt.py -s -m grok-2-vision-1212 /path/to/project
  ```

  Note: Each model has different capabilities and token limits:
  - OpenAI GPT-4: 8K tokens
  - OpenAI GPT-3.5: 4K tokens
  - xAI Grok-2: 130K tokens
  - xAI Grok-2-Vision: 8K tokens

#### Command-line Arguments

- `project_path` (required): Path to your Git project directory.
- `-o, --output`: Specify the output file path (default: `concatenated_source.txt`).
- `-d, --debug`: Enable debug logging to get detailed information about file selection.
- `-n, --no-structure`: Omit the directory structure from the output file.
- `-e, --no-extensions`: Disable file extension filtering (include all files regardless of extension).
- `-s, --summary`: Generate AI documentation summary (requires OpenAI or xAI API key).
- `-m, --model`: Specify custom AI model for summary generation (e.g., 'gpt-4', 'gpt-3.5-turbo' for OpenAI or 'grok-2-1212', 'grok-2-vision-1212' for xAI).

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
2. **Project's `.gitignore`:** If a `.gitignore` is present at the root of your project, CodeSmelt honors its rules.
3. **Directory-specific Rules:** Additional `.gitignore` files in subdirectories will also be considered.

*To customize, modify the `IGNORE_PATTERNS` in `extensions.py`.*

---

## Tips for Using with LLMs

1. **Token Management:**
   - For very large projects, consider concatenating only specific directories to avoid token limits.
   - Use debug mode (`-d`) to verify which files are included/excluded.
   - Choose appropriate AI models based on your project size (xAI models support larger contexts).

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