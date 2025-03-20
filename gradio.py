import gradio as gr

def response(login, senha):
    return "Olá mundo!"

def response2(login, history):
    return "Olá mundo!"

gr.ChatInterface(fn=response2).launch()
# gr.Interface(fn=response, 
#             inputs=[gr.Text(label="Login"), gr.Text(label="Senha")], 
#             outputs="text").launch()