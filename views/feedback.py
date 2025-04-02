# pages/feedback.py
import streamlit as st
from translations import traduzir


def pagina_feedback():
    idioma = st.session_state.get("idioma", "en")
    st.title(traduzir("feedback", idioma))
    st.write(traduzir("descricao_feedback", idioma))

    if "feedback_counter" not in st.session_state:
        st.session_state.feedback_counter = 0

    feedback_placeholder = st.empty()
    feedback_key = f"feedback_text_{st.session_state.feedback_counter}"
    feedback_text = feedback_placeholder.text_area(
        traduzir("mensagem_feedback", idioma), key=feedback_key)

    if st.button(traduzir("enviar_feedback", idioma)):
        if not feedback_text.strip():
            st.error(traduzir("empty_feedback", idioma))
        else:
            with open("feedbacks.txt", "a", encoding="utf-8") as f:
                f.write(
                    f"Usuario: {st.session_state.get('nome_usuario', 'N/A')}\n")
                f.write(f"Feedback: {feedback_text}\n")
                f.write("----\n")
            st.success(traduzir("obrigado_feedback", idioma))
            st.session_state.feedback_counter += 1
            feedback_placeholder.empty()
