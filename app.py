# app.py
import streamlit as st
from translations import traduzir
from views.home import pagina_inicio
from views.instructions import pagina_instrucoes
from views.feedback import pagina_feedback
from views.dmeis import pagina_dmeis
from views.meis import pagina_meis


def configurar_pagina_inicial():
    st.title(traduzir("titulo_app", "en"))
    nome_usuario = st.text_input(traduzir("nome_usuario", "en"))
    idioma_selecionado = st.selectbox(
        "🌐 " + traduzir("selecione_idioma", "en"),
        ["🇺🇸 English", "🇧🇷 Português"],
        index=0
    )
    st.session_state["idioma"] = "pt" if idioma_selecionado == "🇧🇷 Português" else "en"
    if st.button(traduzir("start", st.session_state.get("idioma", "en"))):
        if not nome_usuario:
            st.error(traduzir("erro_nome", st.session_state.get("idioma", "en")))
        else:
            st.session_state.nome_usuario = nome_usuario
            st.session_state.iniciado = True


def carregar_interface():
    idioma = st.session_state.get("idioma", "en")
    st.sidebar.write(
        f"**Usuário:** {st.session_state.get('nome_usuario', '')}")
    st.sidebar.write(f"**Idioma:** {idioma}")
    page = st.sidebar.radio(
        traduzir("navegacao", idioma),
        [
            traduzir("inicio", idioma),
            traduzir("instrucoes", idioma),
            traduzir("meis", idioma),
            traduzir("dmeis", idioma),
            traduzir("feedback", idioma)
        ]
    )
    if page == traduzir("inicio", idioma):
        pagina_inicio()
    elif page == traduzir("instrucoes", idioma):
        pagina_instrucoes()
    elif page == traduzir("meis", idioma):
        pagina_meis()
    elif page == traduzir("dmeis", idioma):
        pagina_dmeis()
    elif page == traduzir("feedback", idioma):
        pagina_feedback()


if "iniciado" not in st.session_state or not st.session_state.iniciado:
    configurar_pagina_inicial()
else:
    carregar_interface()
