import gradio as gr

history = [
    # ["Olá mundo!", "Olá, como você está?"],
]

def response(message, history):
    return "Olá mundo!"

gr.ChatInterface(fn=response).launch()