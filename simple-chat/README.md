# Simple Chat

A lightweight chat application built with React and Tailwind CSS that connects to OpenAI's API.

## Overview

Simple Chat is a web-based chat interface that allows users to interact with OpenAI's language models. The application features a clean, responsive UI with support for Markdown rendering, code syntax highlighting, and streaming responses.

## Features

- Real-time chat interface with OpenAI's language models
- Markdown support with [remark-gfm](https://github.com/remarkjs/remark-gfm)
- Code syntax highlighting via [react-syntax-highlighter](https://github.com/react-syntax-highlighter/react-syntax-highlighter)
- Streaming responses for a more interactive experience
- Responsive design using Tailwind CSS
- Simple Python server with live reload functionality

## Tech Stack

- **Frontend**:
  - React (loaded via CDN)
  - Tailwind CSS (loaded via CDN)
  - Babel for JSX/TSX transpilation
  - Various React libraries (react-markdown, remark-gfm, react-syntax-highlighter)

- **Backend**:
  - Python server using the livereload package
  - OpenAI API for chat functionality

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key
- uv (recommended) - A fast Python package installer and resolver

### Installation

1. Clone the repository or download the source files
2. Navigate to the project directory

#### Installing uv (recommended)

If you don't have uv installed, you can install it using:

```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Configuration

1. Copy `config.json.sample` to `config.json`
2. Open `config.json` and replace the placeholder in the `OPENAI_API_TOKEN` constant with your actual OpenAI API key:

```javascript
{
  "openai": {
      "api_token": "OPENAI_API_TOKEN"
  }
}
```

### Running the Application

1. Start the Python server in current folder
    
    **With http server**
    ```bash
    python -m http.server 8000
    ```
    navigate to [http://localhost:8000](http://localhost:8000)
    
    OR
    
    **With live reload**

    Note: *server will automatically install dependencies*
    ```bash
    python server.py
    ```
    navigate to [http://localhost:5500](http://localhost:5500) (default for livereload)

### Using uv for Development

If you want to manually manage dependencies with uv:

```bash
# Create a virtual environment
uv venv

# Activate the virtual environment
# On macOS/Linux
source .venv/bin/activate
# On Windows
.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Add a new dependency
uv pip install package-name
```

## Usage

- Type your message in the input field at the bottom of the screen
- Press Enter or click the send button (arrow icon) to send your message
- The AI will respond with formatted text, including Markdown and syntax-highlighted code when appropriate
- Use the scroll button to quickly navigate to the bottom of the conversation

## Project Structure

- `index.html` - Main application file containing the React components and application logic
- `server.py` - Simple Python server with live reload functionality
- `tailwind.config.js` - Configuration file for Tailwind CSS

## Customization

The application can be customized by modifying the React components in the `index.html` file. The UI is built with Tailwind CSS, making it easy to adjust styles and layout.

## Limitations

- Performance constraints due to scripts loaded from CDN
- Limited features (intended for demonstration purposes)

## TODO

- Configuration UI to enter credentials and store in local storage
- Configuration toggle for streaming mode
- Upload content and multimodal support

## Roadmap

- Configuration UI to allow selecting agent and LLM
- Pre-configured endpoints for Agents, Models, Custom APIs, etc.
- Display Agent/LLM returned options as pills that users can select for next actions
- Support additional actions after AI response (like, dislike, copy, regenerate, etc.)
- Custom React component for rendering AI Response
- Conversation state display
- Server-side conversation support

## License

This project is open source and available under the MIT License.
