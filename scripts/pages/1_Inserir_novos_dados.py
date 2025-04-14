import streamlit as st 
from connect_db import connection_db, InsereDados

st.set_page_config(
    page_title="Inserir novos dados"
)


with st.form("insere_dados"):
   
   item = st.text_input('Digite o nome do item: ')
   valor = st.number_input('Digite o nome do item: ')
   submit = st.form_submit_button("Salvar item")
   
if submit:
    InsereDados(item,valor)


