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

- Python 3.6+
- OpenAI API key

### Installation

1. Clone the repository or download the source files
2. Navigate to the project directory

### Configuration

1. Open `index.html` and replace the placeholder in the `OPENAI_API_TOKEN` constant with your actual OpenAI API key:

```javascript
const OPENAI_API_TOKEN = "your-openai-api-key-here";
```

### Running the Application

1. Start the Python server:

```bash
python server.py
```

2. The server will automatically install any missing dependencies and start serving the application
3. Open your browser and navigate to `http://localhost:5500` (default port)
4. The server supports live reloading, so any changes to HTML files will automatically refresh the browser

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

## License

This project is open source and available under the MIT License.
