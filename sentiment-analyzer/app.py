# Construção da aplicação de Análise de Sentimento em Python com Streamlit e Hugging Face

# Para executar o código:
# python -m venv venv
# source venv/bin/activate
# pip install transformers streamlit
# streamlit run /Users/leandrowanderley/Documents/programacao/IA-UFAL/sentiment-analyzer/app.py

from transformers import pipeline
import streamlit as st

st.title("Análise de Sentimento")

text = st.text_area("Digite um texto:")

if st.button("Analisar"):
    classifier = pipeline("sentiment-analysis")
    result = classifier(text)[0]
    st.write(f"**Sentimento:** {result['label']} (score: {result['score']:.2f})")
