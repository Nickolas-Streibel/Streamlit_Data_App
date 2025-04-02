# pages/instructions.py
import streamlit as st
from translations import traduzir


def pagina_instrucoes():
    idioma = st.session_state.get("idioma", "en")
    st.title(traduzir("instrucoes", idioma))
    st.write(traduzir("descricao_instrucoes", idioma))
