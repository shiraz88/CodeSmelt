```markdown
# CodeSmelt: Source Code Concatenator

![CodeSmelt Logo](assets/CodeSmeltLogo.jpg)

**CodeSmelt** is a command-line tool designed to simplify the analysis and sharing of Git projects by concatenating source code files into a single file. This tool preserves the directory structure within the output, providing a comprehensive view of the project layout. It is particularly useful for code analysis, input preparation for language models, and sharing project snapshots.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Key Features](#key-features)
- [Core Classes](#core-classes)
- [Notable Algorithms and Patterns](#notable-algorithms-and-patterns)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Tips for Using with LLMs](#tips-for-using-with-llms)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Project Structure

```plaintext
├── README.md
├── ai_integration.py
├── codesmelt.py
├── extensions.py
├── output.txt
├── pyproject.toml
├── requirements.txt
└── assets/
    └── CodeSmeltLogo.jpg
```

### Description of Key Files

- **codesmelt.py**: Main executable script for concatenating source code files.
- **extensions.py**: Contains configuration for file extensions and ignore patterns.
- **requirements.txt**: Lists required dependencies.
- **pyproject.toml**: Project metadata and dependencies declaration.
- **assets/**: Directory containing project assets like the logo.

---

## Key Features

- **Concatenation with Context**: Combines multiple source files into a single file while preserving directory structure.
- **Smart Filtering**: Utilizes file extension whitelists and ignore patterns, respecting `.gitignore` rules.
- **Encoding Handling**: Manages file encoding, defaulting to UTF-8, with a fallback to Latin-1.
- **Debug Logging**: Provides detailed logging to understand file inclusion/exclusion.
- **Customizable Output**: Options to tweak directory structure inclusion and file extension filtering.
- **AI Summary**: Can generate documentation summaries using AI, provided the necessary API keys are set.

---

## Core Classes

### `CodeSmelt`

A class responsible for handling the concatenation process. Key responsibilities include:
- Managing project path and output file setup.
- Filtering files based on extensions and ignore patterns.
- Reading file contents with encoding management.
- Generating directory-like structure within the concatenated output.
- Optionally generating an AI-based summary of the concatenated source code.

---

## Notable Algorithms and Patterns

- **File Filtering**: Uses a combination of file extension checks, ignore patterns, and `.gitignore` parsing for intelligent file selection.
- **Directory Structure Generation**: Recursively traverses directories to build a tree-like structure within the output.
- **Encoding Strategy**: Attempts to read files with UTF-8 encoding and falls back to Latin-1 if necessary.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/codesmelt.git
   cd codesmelt
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure Required Files**:
   Ensure all key files listed in the project structure are present.

---

## Usage

### Basic Usage

To concatenate project source files, run:
```bash
python codesmelt.py /path/to/project
```

### Advanced Options

- **Custom Output File**:
  ```bash
  python codesmelt.py -o output.txt /path/to/project
  ```

- **Enable Debug Logging**:
  ```bash
  python codesmelt.py -d /path/to/project
  ```

- **Exclude Directory Structure**:
  ```bash
  python codesmelt.py -n /path/to/project
  ```

- **Include All Files (Disable Filtering)**:
  ```bash
  python codesmelt.py -e /path/to/project
  ```

- **Generate AI Documentation Summary**:
  ```bash
  python codesmelt.py -s /path/to/project
  ```

### Command-line Arguments

- `project_path` (required): Directory path of the Git project.
- `-o, --output`: Output file path.
- `-d, --debug`: Enable detailed debug logging.
- `-n, --no-structure`: Exclude directory structure from output.
- `-e, --no-extensions`: Include all files, bypassing extension filtering.
- `-s, --summary`: Generate an AI summary if API keys are provided.

---

## Configuration

### Source File Extensions

Defined in `extensions.py`, this set determines which files are included based on their extensions. Customize by editing `SOURCE_EXTENSIONS`.

### Ignore Patterns

`IGNORE_PATTERNS` in `extensions.py` specifies files/directories to exclude. The tool also respects `.gitignore` files for additional filtering.

---

## Tips for Using with LLMs

- **Token Management**: Limit concatenation to essential directories for large projects.
- **Effective Prompting**: Use directory structure references for clarity.
- **Review Output**: Ensure the concatenated file meets your needs before LLM submission.

---

## Troubleshooting

- **Files Not Found**: Validate project path and file extensions. Use `--debug` for insights.
- **Dependencies Missing**: Run `pip install -r requirements.txt`.
- **Permission Issues**: Verify read/write permissions for involved directories and files.

---

## Contributing

Contributions are welcome! Fork the repository and submit pull requests for improvements, bug fixes, or new features. Discuss major changes via issues first.

---

## License

Licensed under the [MIT License](LICENSE).

---

## Author

**Shiraz Akmal**

Contact via [Twitter](https://x.com/ShirazAkmal) for questions or feedback.

Happy coding with CodeSmelt!
```