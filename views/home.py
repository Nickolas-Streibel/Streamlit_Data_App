# pages/home.py
import streamlit as st
from translations import traduzir


def pagina_inicio():
    idioma = st.session_state.get("idioma", "en")
    st.title(traduzir("bem_vindo", idioma))
    st.write(traduzir("descricao_inicio", idioma))
    st.markdown(
        f"<hr><p style='text-align: center;'>{traduzir('creditos', idioma)}</p>",
        unsafe_allow_html=True
    )
