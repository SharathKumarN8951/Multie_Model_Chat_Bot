# Multie_Model_Chat_Bot
Image • PDF • Conversational Memory
A multi-modal AI chatbot built using Streamlit and Groq LLaMA-3, capable of answering user queries by combining PDF content, image context, and chat history within a single conversational interface.
Features

💬 Conversational AI Chatbot

📄 PDF-based Question Answering

🖼️ Image-aware reasoning (context-based)

🧠 Persistent chat memory using Streamlit session state

⚡ Fast inference powered by Groq (LLaMA-3)

🌐 Interactive web interface using Streamlit

🏗️ System Architecture

User Input → Multi-Modal Fusion → LLM Response

User uploads a PDF and/or Image

Text is extracted from the PDF

Image context is added as descriptive metadata

Chat history is preserved across turns

All modalities are fused into a single prompt

LLaMA-3 generates a context-aware response

🛠️ Tech Stack

Programming Language: Python

Frontend: Streamlit

LLM Backend: Groq (LLaMA-3)

PDF Parsing: PyPDF

Image Handling: Pillow (PIL)

Environment Management: python-dotenv
