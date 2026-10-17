# Ollama AI Chatbot

A simple interactive AI chatbot built using Python, Ollama, and the Qwen 3.5 0.8B language model. It runs locally and allows users to have conversations through the terminal.

## Features

- Interactive terminal-based chatbot
- Powered by the Qwen 3.5 0.8B model
- Maintains conversation history during the current session
- Customizable AI response settings
- Runs locally using Ollama

## Technologies Used

- Python
- Ollama
- Qwen 3.5 0.8B

## Prerequisites

- Python installed on your computer
- Ollama installed and running
- Qwen 3.5 0.8B model downloaded locally

## Installation

### 1. Install Ollama

Download it from https://ollama.com/

### 2. Download the model

```bash
ollama pull qwen3.5:0.8b
```

### 3. Clone this repository

```bash
git clone YOUR_REPOSITORY_URL
cd ollama-ai-chatbot
```

Replace `YOUR_REPOSITORY_URL` with your repository URL.

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the chatbot

```bash
python prompt2.py
```

## Usage

Enter a message in the terminal to receive an AI-generated response. Type `exit` to end the conversation.

## Project Structure

```text
ollama-ai-chatbot/
├── prompt2.py
├── requirements.txt
└── README.md
```

## Note

The language model runs locally through Ollama and is not included in this repository. Response speed depends on your hardware.

## License

For educational and personal use.
