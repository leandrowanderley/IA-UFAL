# Import for chatbot
import gradio as gr

# Imports for generate responses
import google.generativeai as genai
import json

# Configure AI model
with open("key-gemini.json") as f:
    api_key = json.load(f)["key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_response(message):
    try:
        response = model.generate_content(message)
        return response.text.strip()
    except Exception as e:
        return f"Sorry, I am not able to respond to that, um erro ocorreu: {e}"

# Inicial idea of history messages
history = []

def response_chatbot(message, history):
    return generate_response(message)

gr.ChatInterface(fn=response_chatbot).launch()