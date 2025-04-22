# Baseadas em Regras (Linguísticas)
# source venv/bin/activate
# pip install vaderSentiment
# streamlit run vader.py

# Calcula 4 scores:
# pos → Positividade
# neu → Neutralidade
# neg → Negatividade
# compound → Score composto (de -1 a 1)

# O serviço foi INCRÍVEL!!!

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st

st.title("Análise de Sentimento com Vader")

text = st.text_area("Digite um texto:")

if st.button("Analisar"):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    
    st.write("**Pontuações:**", scores)
    
    if scores['compound'] >= 0.35:
        st.success("Sentimento: Positivo 😊")
    elif scores['compound'] <= -0.25:
        st.error("Sentimento: Negativo 😠")
    else:
        st.info("Sentimento: Neutro 😐")
