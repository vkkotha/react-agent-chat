# React Agent Chat

This repository contains various chat-related projects focused on implementing AI-powered conversational interfaces.

## Projects

### simple-chat
A lightweight chat application built with React and Tailwind CSS that connects to OpenAI's API. The goal is to maintain simplicity with everything contained in a single HTML file that can be served by any web server.

<p align="center">
  <img src="https://github.com/user-attachments/assets/df831432-b0c3-4094-8241-e8322e94ee7f" width="80%"/>
</p>

#### Features:
- Single HTML page UI with minimal dependencies
- AI & User message display
- Multiline chat input with Send action and working indicator
- Streaming chat output
- Automatic scroll to bottom
- Hidden scrollbars for cleaner interface
- Formatted code and markdown in responses

#### Limitations:
- Performance constraints due to scripts loaded from CDN
- Limited features (intended for demonstration purposes)

#### TODO:
- Configuration UI to enter credentials and store in local storage
- Configuration toggle for streaming mode
- Upload content and multimodal support
  
#### Roadmap:
- Configuration UI to allow selecting agent and LLM
- Pre-configured endpoints for Agents, Models, Custom APIs, etc.
- Display Agent/LLM returned options as pills that users can select for next actions
- Support additional actions after AI response (like, dislike, copy, regenerate, etc.)
- Custom React component for rendering AI Response
- Conversation state display
- Server-side conversation support

## License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
