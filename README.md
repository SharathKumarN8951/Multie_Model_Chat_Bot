# Multi-Model Chat Bot

This project is an AI-powered chatbot built using Python, Streamlit, and Groq LLMs. The application allows users to interact with different AI models through a single interface and supports multiple input formats, including text, images, and files.

The goal of this project was to create a versatile chatbot that can handle different types of user inputs and provide intelligent responses in real time.

**Live Demo:**
https://multiemodelchatbot-dczh2higfymjp5dbnb8rwb.streamlit.app/

## About the Project

Most chatbot applications focus only on text-based conversations. In this project, I wanted to build a more flexible AI assistant that can understand not only text prompts but also uploaded images and files.

The chatbot uses Groq's fast inference capabilities to generate responses and provides an easy-to-use interface built with Streamlit.

## Features

* Chat with AI using text prompts
* Upload and analyze images
* Upload files and ask questions about their content
* Multiple model support through Groq
* Simple and responsive Streamlit interface
* Real-time AI-generated responses

## Technologies Used

* Python
* Streamlit
* Groq API
* Large Language Models (LLMs)
* Environment Variables (.env)

## Project Structure

```text
Multie_Model_Chat_Bot/
│
├── Chat_Bot.py
├── requirements.txt
├── README.md
├── LICENSE
└── .devcontainer/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/SharathKumarN8951/Multie_Model_Chat_Bot.git
```

Move to the project directory:

```bash
cd Multie_Model_Chat_Bot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your API key:

```env
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run Chat_Bot.py
```

## How It Works

1. Users can enter a text prompt or upload a file/image.
2. The application processes the input.
3. The selected Groq model receives the request.
4. The AI generates a response based on the provided content.
5. The response is displayed instantly in the chat interface.

## What I Learned

Through this project, I gained practical experience in:

* Building AI-powered applications
* Integrating Groq APIs
* Handling file and image uploads
* Working with Large Language Models
* Creating interactive web applications using Streamlit

## Future Improvements

Some features I would like to add in future versions:

* Conversation history storage
* User authentication
* Voice-based interaction
* Support for additional AI models
* Better document analysis capabilities
* Export chat functionality

## Author

**Sharath Kumar N**

GitHub: https://github.com/SharathKumarN8951

