import streamlit as st
import pandas as pd
from back import recomendar_notebook

if 'past_cases' not in st.session_state:
    st.session_state.past_cases = []
    st.session_state.preferences = []


st.title("Sistema Especialista em Notebooks")

# Introdução e instruções
st.write("Bem-vindo ao sistema especialista em Notebooks!")

prices = st.slider("Escolha o Preço médio desejado", 1500, 10000, step=500)

options = ['Asus', 'Lenovo', 'MSI', 'Apple', 'Hp', 'Acer', 'Dell']
finality = ['Gamer', 'Casual', 'Work']

selected_options = st.selectbox("Selecione a Marca Desejada", options)
selected_finality = st.radio("Selecione a Finalidade Desejada", finality)

if st.button("Obter seu Laptop Ideal"):
    # Armazenar os valores selecionados em uma lista
    valores_selecionados = ([prices, selected_finality, selected_options], None)

    # Adicionar a lista ao estado da sessão
    # st.session_state.past_cases.append(valores_selecionados)
    notebook_recomendado = recomendar_notebook(valores_selecionados)

    # Exibir os valores armazenados
    if notebook_recomendado:
        st.write("Seu Notebook:", notebook_recomendado)
    else:
        st.write("Nenhum Notebook foi encontrado para essas especificações")
