import streamlit as st
from connect_db import ObtemDados
import pandas as pd

st.set_page_config(
    page_title="Home"
)

dados=ObtemDados()

df=pd.DataFrame(dados,columns=["ID", "NOME", "VALOR"])

st.dataframe(df.style.highlight_max(axis=0))