# Baseadas em Regras (Linguísticas)
# source venv/bin/activate
# pip install scikit-learn pandas streamlit
# streamlit run naive_bayes.py

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Dados simples de exemplo
data = {
    'texto': [
        "Eu adorei o filme, foi excelente!",
        "O filme foi horrível, perdi meu tempo.",
        "Gostei muito, super recomendo.",
        "Péssimo. Atuação fraca e enredo ruim.",
        "Um dos melhores filmes que já vi!",
        "Que decepção. História sem graça.",
    ],
    'sentimento': ['positivo', 'negativo', 'positivo', 'negativo', 'positivo', 'negativo']
}

df = pd.DataFrame(data)

# Treinando o modelo
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(df['texto'], df['sentimento'])

# App com Streamlit
st.title("Análise de Sentimento com ML tradicional 🤖")

user_text = st.text_area("Digite um texto:")

if st.button("Analisar"):
    prediction = model.predict([user_text])[0]
    proba = model.predict_proba([user_text])[0]

    st.write(f"**Sentimento previsto:** {prediction}")
    st.write(f"**Confiança:** {max(proba) * 100:.2f}%")
