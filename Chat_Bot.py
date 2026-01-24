## import the necessary libraries
import streamlit as st
import os
from langchain_groq import ChatGroq
from pypdf import PdfReader
from PIL import Image
from dotenv import load_dotenv


load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")                            ## Add your Api key and Model name get it from a langchain_groq
llm=ChatGroq(model_name="openai/gpt-oss-120b")

# chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# store pdf & image context
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

if "image_desc" not in st.session_state:
    st.session_state.image_desc = ""

## creating a funtion for the pdf reader
def read_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text[:3000]   # token limit

## creating a function for the image reader
def analyze_image(image):
    return "An image was uploaded. Consider visible objects, colors, and patterns."

## This is a multimodel chat bot it cannot anlyse the image perfectly this model is text based 
def multimodal_chat(question, pdf_text, image_desc):

    history_text = ""
    for chat in st.session_state.chat_history:
        history_text += f"User: {chat['user']}\nAssistant: {chat['assistant']}\n"

    prompt = f"""
You are an intelligent multi-modal assistant.

Chat History:
{history_text}

PDF Content:
{pdf_text}

Image Description:
{image_desc}

User Question:
{question}

Answer clearly and accurately.
"""

    response = llm.invoke(prompt)

    # Saves conversation in the memory 
    st.session_state.chat_history.append({
        "user": question,
        "assistant": response.content
    })

    return response.content

### Stremlit UI frontend
st.title("🧠 Multi-Modal AI Chatbot")

uploaded_pdf = st.file_uploader("📄 Upload PDF", type=["pdf"])
uploaded_image = st.file_uploader("🖼️ Upload Image", type=["png", "jpg", "jpeg"])

## displayes a chat history
for chat in st.session_state.chat_history:
    st.chat_message("user").write(chat["user"])
    st.chat_message("assistant").write(chat["assistant"])

## input box
question = st.chat_input("Ask your question")

## processing a user uploader files like image, pdf, text
if uploaded_pdf:
    st.session_state.pdf_text = read_pdf(uploaded_pdf)
    st.success("PDF loaded successfully!")

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", width=800)
    st.session_state.image_desc = analyze_image(image)

## handeling a user query
if question:
    st.chat_message("user").write(question)
    answer = multimodal_chat(
        question,
        st.session_state.pdf_text,
        st.session_state.image_desc
    )
    st.chat_message("assistant").write(answer)

