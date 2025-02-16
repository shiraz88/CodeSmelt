# CodeSmelt README

## Table of Contents

- [Project Structure](#project-structure)
- [Key Features](#key-features)
- [Core Classes](#core-classes)
- [Notable Algorithms and Patterns](#notable-algorithms-and-patterns)
- [Dependencies and Requirements](#dependencies-and-requirements)

---

## Project Structure

The project structure is organized as follows:

```plaintext
├── README.md
├── ai_integration.py
├── codesmelt.py
├── extensions.py
├── output.summary.md
├── output.txt
├── pyproject.toml
├── requirements.txt
└── assets/
    └── CodeSmeltLogo.jpg
```

### Description of Key Files

- **README.md**: Contains detailed instructions on how to use the tool, its features, and configuration options.
- **ai_integration.py**: Handles integration with AI services for generating documentation summaries.
- **codesmelt.py**: The main executable script responsible for concatenating source code files.
- **extensions.py**: Defines configurations for file extensions and ignore patterns.
- **output.txt**: The default output file where the concatenated source code is written.
- **output.summary.md**: The output file for AI-generated documentation summaries.
- **pyproject.toml**: Contains project metadata and dependencies.
- **requirements.txt**: Lists the required Python packages for the project.
- **assets/**: A directory containing project assets like the logo.

---

## Key Features

- **Concatenation with Context**: Combines multiple source files into a single file while preserving the directory structure. This provides a clear layout of the project in the output file.
- **Smart Filtering**: Utilizes file extension whitelists and ignore patterns to intelligently select files. It also respects `.gitignore` rules for additional filtering.
- **Encoding Handling**: Manages file encoding, defaulting to UTF-8, with a fallback to Latin-1 to ensure all files can be read.
- **Debug Logging**: Offers detailed logging to help users understand which files are included or excluded from the concatenation process.
- **Customizable Output**: Allows users to tweak the output by omitting the directory structure or disabling file extension filtering.
- **AI Documentation Summary**: Optionally generates a documentation summary using AI, provided the necessary API keys are set.

---

## Core Classes

### `CodeSmelt` (from `codesmelt.py`)

The `CodeSmelt` class is the core component of the tool and is responsible for the concatenation process. Its key responsibilities include:

- **Project Path and Output Setup**: Manages the project directory path and the output file setup.
- **File Filtering**: Determines which files should be included based on extensions, ignore patterns, and `.gitignore` rules.
- **File Reading**: Reads file contents with proper encoding handling, attempting UTF-8 first and falling back to Latin-1 if needed.
- **Directory Structure Generation**: Recursively traverses directories to generate a tree-like structure within the output file.
- **AI Summary Generation**: Optionally generates an AI-based summary of the concatenated source code if the `-s` flag is used.

### `OpenAI` (from `ai_integration.py`)

The `OpenAI` class is used to interface with AI services for generating documentation summaries. It provides methods to:

- **Initialize AI Client**: Sets up the client using environment variables for API keys.
- **Generate Summary**: Sends the concatenated source code to the AI service to generate a comprehensive documentation summary.

---

## Notable Algorithms and Patterns

- **File Filtering Algorithm**: Employs a multi-level filtering approach using file extension checks, predefined ignore patterns, and `.gitignore` parsing. This ensures that only relevant files are included in the output.
- **Directory Structure Generation**: Utilizes a recursive algorithm to traverse the project directory and build a tree-like structure within the output file, which helps in visualizing the project layout.
- **Encoding Strategy**: Implements a strategy pattern for reading files, trying UTF-8 encoding first and falling back to Latin-1 if necessary, ensuring robust file handling.

---

## Dependencies and Requirements

### Python Version

- **Python 3.11 or higher** is required to run CodeSmelt.

### Dependencies

The following Python packages are required and can be installed using the `requirements.txt` file:

- **gitignore-parser**: Version 0.1.11 or higher for parsing `.gitignore` files.
- **openai**: For integration with OpenAI's AI services to generate documentation summaries.

To install these dependencies, run:

```bash
pip install -r requirements.txt
```

### Optional Dependencies

- **xAI**: For using xAI's API instead of OpenAI's, which requires setting the `XAI_API_KEY` environment variable.

### Environment Variables

For AI integration, the following environment variables need to be set:

- `OPENAI_API_KEY`: Required for using OpenAI's API.
- `XAI_API_KEY`: Required for using xAI's API.