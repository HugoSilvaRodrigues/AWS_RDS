import streamlit as st

from connect_db import cria_branco

with st.form("Criação do banco"):
    nome=st.text_input("Digite o nome do banco: ")
    submit=st.form_submit_button("Criar banco")

if submit:
    cria_branco(nome)
