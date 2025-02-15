"""
Source code file extension configurations
"""

# Common source code file extensions
SOURCE_EXTENSIONS = {
    # Web
    '.js', '.ts', '.jsx', '.tsx', '.vue', '.svelte',
    '.html', '.htm', '.css', '.scss', '.sass', '.less',
    
    # Python
    '.py', '.pyi', '.pyx',
    
    # Java/Kotlin
    '.java', '.kt', '.groovy',
    
    # C-family
    '.c', '.cpp', '.h', '.hpp', '.cc',
    
    # C#
    '.cs', '.cshtml', '.csx',
    
    # Ruby
    '.rb', '.erb',
    
    # PHP
    '.php', '.php5', '.phtml',
    
    # Go
    '.go',
    
    # Rust
    '.rs',
    
    # Swift
    '.swift',
    
    # Shell
    '.sh', '.bash', '.zsh',
    
    # Config/Data
    '.json', '.yaml', '.yml', '.toml', '.xml',
    '.conf', '.ini', '.env',
    
    # Documentation
    '.md', '.rst', '.txt'
}

# Files to always ignore
IGNORE_PATTERNS = {
    # Build outputs
    'build/*', 'dist/*', 'target/*', 'bin/*',
    '*.pyc', '__pycache__/*', '*.class',
    
    # Dependencies
    'node_modules/*', 'vendor/*', 'venv/*',
    
    # IDE files
    '.idea/*', '.vscode/*', '*.swp',
    
    # Package files
    'package-lock.json', 'yarn.lock',
    'Pipfile.lock', 'poetry.lock',
    
    # Large data files
    '*.csv', '*.json.gz', '*.sql',
    
    # Binary/Media files
    '*.pdf', '*.jpg', '*.png', '*.gif',
    '*.mp3', '*.mp4', '*.mov', '*.bin',
    '*.exe', '*.dll', '*.so', '*.dylib'
}
