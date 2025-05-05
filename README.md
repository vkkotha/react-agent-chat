# React Agent Chat

This repository contains various chat-related projects.

## Projects

### simple-chat
A lightweight chat application built with React and Tailwind CSS that connects to OpenAI's API. The goal is to keep everything in single html file and serve up with any websever.

<p align="center">
  <img src="https://github.com/user-attachments/assets/df831432-b0c3-4094-8241-e8322e94ee7f" width="80%"/>
</p>

Features:
- Very simple single html page UI.
- AI & User messages.
- Multiline chat Input with with Send action, working indicator.
- Streaming chat output.
- Scroll to bottom.
- Hide scrollbars.
- Format code and markdown in responses.

Limitations:
- Slow as the scripts are loaded from CDN.
- Limited features for demonstration purpose.

TODO:
- Configuraiton UI to enter credentials and store in local storage.
- Configuration to toggle streaming mode.
- Upload content and Multimodal support.
  
Roadmap:
- Configuration UI to allow selecting agent, llm.
- Pre Configured endpoints like Agents, Models, Custom APIs etc..
- Show Agent/LLM returned options as pills, that user can select as next action.
- Support additional actions after AI response. Ex: like, dislike, copy, regenerate etc...
- Custom react component for rendering AI Repsonse.
- Showing Conversation state along side.
- Supporting server side conversation.
