# pages/meis.py
import streamlit as st
import numpy as np
from translations import traduzir
from data_processing import load_data
from plotting import plot_data
import io


def save_sum_scan_txt(sum_scan):
    buffer = io.StringIO()
    np.savetxt(buffer, sum_scan, fmt='%.6e')
    buffer.seek(0)
    return buffer


def pagina_meis():
    idioma = st.session_state.get("idioma", "en")
    st.title(traduzir("meis", idioma))
    uploaded_files = st.file_uploader(traduzir(
        "selecione_arquivos_meis", idioma), type=["txt"], accept_multiple_files=True)
    if uploaded_files:
        try:
            sum_scan = load_data(
                uploaded_files, lambda chave: traduzir(chave, idioma))
            st.session_state['sum_scan'] = sum_scan
            data_log = np.log((sum_scan / 2) + 1)
            energy = sum_scan[:, 0]
            theta = sum_scan[0, 1:]
            dtheta = 0.08
            st.subheader(traduzir("visualizacao_grafico", idioma))
            plot_data(data_log, energy, theta, dtheta,
                      lambda chave: traduzir(chave, idioma))
            buffer = save_sum_scan_txt(sum_scan)
            st.download_button("Download sum_scan.txt",
                               buffer.getvalue(), "sum_scan.txt", "text/plain")
        except Exception as e:
            st.error(str(e))
    elif 'sum_scan' in st.session_state:
        sum_scan = st.session_state['sum_scan']
        data_log = np.log((sum_scan / 2) + 1)
        energy = sum_scan[:, 0]
        theta = sum_scan[0, 1:]
        dtheta = 0.08
        st.subheader(traduzir("visualizacao_grafico", idioma))
        plot_data(data_log, energy, theta, dtheta,
                  lambda chave: traduzir(chave, idioma))
        buffer = save_sum_scan_txt(sum_scan)
        st.download_button("Download sum_scan.txt",
                           buffer.getvalue(), "sum_scan.txt", "text/plain")
