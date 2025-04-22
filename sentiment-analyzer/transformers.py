# Construção da aplicação de Análise de Sentimento em Python com Streamlit, Hugging Face e transformers

# Tipo de técnica: Deep Learning com arquitetura Transformer
# Base de treinamento: SST-2 (Stanford Sentiment Treebank v2)
# Tipo de análise: Classificação binária (positivo ou negativo)

# Transformers: Arquitetura poderosa baseada em atenção (self-attention), que entende o contexto de palavras mesmo quando estão distantes entre si.

# DistilBERT: Versão reduzida e mais leve do BERT (modelo de linguagem contextualizado da Google).

# Mantém 97% da performance do BERT original com metade do tamanho.

# Fine-tuning: O modelo foi ajustado (refinado) com um conjunto de dados específico de sentimentos (SST-2), tornando-o eficaz nessa tarefa.

# O código utiliza aprendizado profundo com Transformers, mais precisamente o modelo DistilBERT, que já vem treinado para classificar sentimentos com alta precisão.

# Se quiser, posso te mostrar como mudar o modelo, usar modelos em português, ou até treinar um modelo seu com dados específicos! Quer explorar alguma dessas opções?

# Para executar o código:
# python -m venv venv
# source venv/bin/activate
# pip install transformers streamlit
# streamlit run /Users/leandrowanderley/Documents/programacao/IA-UFAL/sentiment-analyzer/app.py

from transformers import pipeline
import streamlit as st

st.title("Análise de Sentimento com Transformers")

text = st.text_area("Digite um texto:")

if st.button("Analisar"):
    classifier = pipeline("sentiment-analysis")
    result = classifier(text)[0]
    st.write(f"**Sentimento:** {result['label']} (score: {result['score']:.2f})")
