import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_text
import matplotlib.pyplot as plt
from sklearn import tree

data = {
    'Histórico de Crédito': [
        'Ruim', 'Desconhecido', 'Desconhecido', 'Desconhecido', 'Desconhecido',
        'Desconhecido', 'Ruim', 'Ruim', 'Boa', 'Boa', 'Boa', 'Boa', 'Boa',
        'Ruim', 'Desconhecido', 'Boa', 'Ruim', 'Boa', 'Desconhecido', 'Boa'
    ],
    'Dívida': [
        'Alta', 'Alta', 'Baixa', 'Baixa', 'Baixa', 'Baixa', 'Baixa', 'Baixa', 
        'Baixa', 'Alta', 'Alta', 'Alta', 'Alta', 'Alta', 'Alta', 'Baixa', 
        'Baixa', 'Baixa', 'Alta', 'Alta'
    ],
    'Garantia': [
        'Nenhuma', 'Nenhuma', 'Nenhuma', 'Nenhuma', 'Nenhuma', 'Adequada', 
        'Nenhuma', 'Adequada', 'Nenhuma', 'Adequada', 'Nenhuma', 'Nenhuma', 
        'Nenhuma', 'Nenhuma', 'Adequada', 'Nenhuma', 'Adequada', 'Adequada', 
        'Nenhuma', 'Adequada'
    ],
    'Renda': [
        '$0 a $15k', '$15k a $35k', '$15k a $35k', '$0 a $15k', 'Acima de $35k',
        'Acima de $35k', '$0 a $15k', 'Acima de $35k', 'Acima de $35k', 
        'Acima de $35k', '$0 a $15k', '$15k a $35k', 'Acima de $35k', '$15k a $35k',
        '$15k a $35k', '$15k a $35k', '$15k a $35k', '$0 a $15k', 'Acima de $35k',
        '$15k a $35k'
    ],
    'Risco': [
        'Alto', 'Alto', 'Moderado', 'Alto', 'Baixo', 'Baixo', 'Alto', 'Moderado',
        'Baixo', 'Baixo', 'Alto', 'Moderado', 'Baixo', 'Alto', 'Moderado', 'Baixo',
        'Moderado', 'Baixo', 'Baixo', 'Moderado'
    ]
}

df = pd.DataFrame(data)

le = LabelEncoder()

for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = le.fit_transform(df[column])

x = df.drop('Risco', axis=1)
y = df['Risco']

clf_cart = DecisionTreeClassifier(criterion='gini', max_depth=3)
clf_cart.fit(x, y)

tree_rules_cart = export_text(clf_cart, feature_names=x.columns.tolist())
print("Árvore de Decisão (Regras - CART):\n", tree_rules_cart)

plt.figure(figsize=(12,8))
tree.plot_tree(clf_cart, filled=True, feature_names=x.columns, class_names=le.classes_)
plt.show()
