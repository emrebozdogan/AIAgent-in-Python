# Python AI Agent

A Python-based AI agent that uses Google's Gemini model to perform coding tasks through natural language commands. The agent can read files, list directories, execute Python scripts, and write files within a sandboxed environment.

## Features

- 🤖 **AI-Powered**: Uses Google Gemini 2.0 Flash for intelligent code understanding
- 📁 **File Operations**: Read, write, and list files and directories
- 🐍 **Code Execution**: Run Python files with optional arguments
- 🔒 **Sandboxed Environment**: Secure execution within designated working directory
- 💬 **Natural Language Interface**: Simple command-line interface for complex operations
- 🔄 **Function Calling**: Automated function planning and execution

## Installation

### Prerequisites

- Python 3.13+
- Google Gemini API key

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/python-ai-agent.git
   cd python-ai-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # or using uv
   uv sync
   ```

3. **Set up environment variables**
   ```bash
   # Create .env file
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

4. **Activate virtual environment** (if using uv)
   ```bash
   source .venv/bin/activate
   ```

## Usage

### Basic Usage

```bash
python main.py "your natural language command here"
```

### Examples

```bash
# List files in the calculator directory
python main.py "show me all files in the calculator directory"

# Read a specific file
python main.py "read the contents of calculator/main.py"

# Run a Python file
python main.py "run the calculator main.py file"

# Write a new file
python main.py "create a new file called hello.py with a simple hello world program"

# Complex operations
python main.py "analyze the calculator code and create a summary of what it does"
```

### Verbose Mode

Add `--verbose` flag to see detailed execution information:

```bash
python main.py --verbose "read calculator/main.py"
```

## Project Structure

```
python-ai-agent/
├── main.py                 # Main entry point
├── call_function.py        # Function calling mechanism
├── functions/              # AI agent function modules
│   ├── config.py          # Configuration settings
│   ├── get_file_content.py # File reading functionality
│   ├── get_files_info.py   # Directory listing functionality
│   ├── run_python_file.py  # Python execution functionality
│   ├── system_prompt.py    # AI system instructions
│   └── write_file.py       # File writing functionality
├── calculator/             # Example project for testing
│   ├── main.py
│   ├── pkg/
│   │   ├── calculator.py
│   │   └── render.py
│   └── tests.py
├── tests.py               # Test suite
├── pyproject.toml         # Project configuration
└── README.md              # This file
```

## Available Functions

The AI agent has access to the following functions:

- **`get_file_content`**: Read contents of any file
- **`get_files_info`**: List files and directories
- **`run_python_file`**: Execute Python scripts with arguments
- **`write_file`**: Create or overwrite files

## Configuration

### Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini API key (required)

### Settings

Edit `functions/config.py` to modify:
- `MAX_ITERS`: Maximum number of function call iterations (default: 10)

## Security

- All file operations are restricted to the `./calculator` directory by default
- The working directory is automatically injected for security
- No direct access to system files or sensitive directories

## Testing

Run the test suite:

```bash
python tests.py
```

## Dependencies

- `google-genai==1.12.1`: Google Gemini AI client
- `python-dotenv==1.1.0`: Environment variable management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues and questions, please open an issue on GitHub.
