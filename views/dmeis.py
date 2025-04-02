# pages/dmeis.py
import streamlit as st
import time
import numpy as np
from translations import traduzir
from data_processing import read_file, angle_sum, rebine, export_spectrum, load_spectrum_file
from plotting import plot_spectrum_with_save, plot_combined_spectra
import plotly.colors


def reset_dmeis_vars():
    valores_padrao = {
        "amin": 108.0,  # Filtro de dados
        "amax": 110.0,
        "denergy": 0.1,
        "angle_min": 108.0,  # Angulo inicial medido
        "angle_bin_size": 0.08
    }
    for chave, valor in valores_padrao.items():
        st.session_state[chave] = valor
    if "reset_counter" not in st.session_state:
        st.session_state["reset_counter"] = 0
    st.session_state["reset_counter"] += 1


def pagina_dmeis():
    idioma = st.session_state.get("idioma", "en")
    st.title(traduzir("dmeis", idioma))

    # Verifica se os parâmetros necessários estão definidos; não resetamos "angle_min"
    if ('amin' not in st.session_state or
        'amax' not in st.session_state or
        'denergy' not in st.session_state or
            'angle_bin_size' not in st.session_state):
        reset_dmeis_vars()

    # "angle_min" já deve estar definido (vindo dos dados do MEIS) e não será alterado aqui.
    if 'exp' not in st.session_state:
        st.session_state['exp'] = None

    if st.button(traduzir("reset_titulo", idioma), help=traduzir("reset_dmeis_help", idioma)):
        reset_dmeis_vars()
        st.success(traduzir("valores_redefinidos", idioma))
        time.sleep(0.5)
        st.rerun()

    reset_counter = st.session_state.get("reset_counter", 0)

    uploaded_file = st.file_uploader(
        traduzir("escolha_arquivo_espectro", idioma), type="txt")
    if uploaded_file:
        try:
            exp = read_file(
                uploaded_file, lambda chave: traduzir(chave, idioma))
            st.session_state['exp'] = exp
            st.session_state['uploaded_file'] = uploaded_file
        except Exception as e:
            st.error(str(e))

    tabs = st.tabs([
        traduzir("parametros_analise", idioma),
        traduzir("grafico_espectro_rebinado", idioma),
        traduzir("resumo_estatistico", idioma),
        traduzir("comparacao_espectros", idioma)
    ])

    with tabs[0]:
        st.subheader(traduzir("parametros_analise", idioma))
        # Apenas os parâmetros que o usuário pode alterar: amin, amax e denergy.
        col1, col2, col3 = st.columns(3)
        with col1:
            amin = st.number_input(traduzir("titulo_amin", idioma),
                                   value=st.session_state.get("amin", 108.0),
                                   step=0.1,
                                   format="%.1f",
                                   key=f"amin_{reset_counter}",
                                   help=traduzir("ajuda_amin", idioma)
                                   )
        with col2:
            amax = st.number_input(
                traduzir("titulo_amax", idioma),
                value=st.session_state.get("amax", 110.0),
                step=0.1,
                format="%.1f",
                key=f"amax_{reset_counter}",
                help=traduzir("ajuda_amax", idioma)
            )
        with col3:
            denergy = st.number_input(
                traduzir("titulo_denergy", idioma),
                min_value=0.01,
                max_value=1.0,
                value=st.session_state.get("denergy", 0.1),
                step=0.01,
                format="%.2f",
                key=f"denergy_{reset_counter}",
                help=traduzir("ajuda_denergy", idioma)
            )

        if amin >= amax:
            st.error(traduzir("angle_min_menor_que_amax", idioma))

        # Atualiza os valores modificáveis
        st.session_state["amax"] = amax
        st.session_state["denergy"] = denergy
        st.session_state["amin"] = amin
        # st.session_state["angle_min"] e st.session_state["angle_bin_size"] permanecem fixos

        if st.button(traduzir("atualizar_grafico", idioma)):
            if st.session_state.get('exp') is None:
                st.error(traduzir("erro_sem_arquivo", idioma))
            else:
                with st.spinner(traduzir("gerando_grafico", idioma)):
                    exp_sum = angle_sum(
                        st.session_state["exp"],
                        st.session_state["angle_min"],
                        st.session_state["angle_bin_size"],
                        st.session_state["amin"],
                        st.session_state["amax"]
                    )
                    exp_final = rebine(exp_sum, st.session_state["denergy"])
                    st.session_state["exp_final"] = exp_final

                    # Atualiza o arquivo para download
                    espectro_txt = export_spectrum(exp_final)
                    st.session_state["spectrum_txt"] = espectro_txt

                st.success(traduzir("atualizacao_concluida", idioma))

    with tabs[1]:
        st.subheader(traduzir("grafico_espectro_rebinado", idioma))
        if st.session_state.get("exp_final") is not None:
            plot_spectrum_with_save(
                st.session_state["exp_final"], lambda chave: traduzir(chave, idioma))
            espectro_txt = st.session_state.get("spectrum_txt", None)
            if espectro_txt:
                st.download_button("Download spectrum.txt",
                                   espectro_txt, "spectrum.txt", "text/plain")
        else:
            st.info(traduzir("info", idioma))

    with tabs[2]:
        st.subheader(traduzir("resumo_estatistico", idioma))
        if st.session_state.get("exp_final") is not None:
            exp_final = st.session_state["exp_final"]
            averages = [np.mean(counts) for counts in exp_final.counts]
            data = {
                traduzir("energia", idioma): exp_final.energy,
                traduzir("average_counts_by_energy", idioma): averages
            }
            import pandas as pd
            df = pd.DataFrame(data)
            st.dataframe(df)
        else:
            st.info(traduzir("no_summary_available", idioma))

    with tabs[3]:
        st.subheader(traduzir("comparacao_espectros", idioma))

        uploaded_files = st.file_uploader(
            traduzir("seleciona_espectros", idioma),
            type="txt",
            accept_multiple_files=True
        )

        if uploaded_files:
            spectra = []
            for file in uploaded_files:
                try:
                    df = load_spectrum_file(file)
                    spectra.append(df)
                except Exception as e:
                    st.error(
                        f"{traduzir('erro_carregar_arquivo', idioma)} {file.name}: {e}")

            if len(spectra) >= 1:
                st.markdown("---")
                st.subheader(traduzir("configuracoes_visualizacao", idioma))

                # Cria colunas para organizar os controles
                col1, col2 = st.columns(2)
                with col1:
                    linewidth = st.slider(
                        traduzir("largura_linha", idioma),
                        min_value=1, max_value=5, value=2
                    )

                    dash_styles = st.multiselect(
                        traduzir("padrao_linhas", idioma),
                        options=["solid", "dot", "dash",
                                 "longdash", "dashdot"],
                        default=["solid"]
                    )
                    if not dash_styles:
                        st.error(traduzir("erro_selecao_linhas", idioma))
                        st.stop()

                with col2:
                    plot_mode = st.selectbox(
                        traduzir("modo_exibicao", idioma),
                        options=["lines", "markers", "lines+markers"],
                        index=0
                    )
                    show_legend = st.checkbox(
                        traduzir("mostrar_legenda", idioma), value=True)

                st.markdown(f"**{traduzir('seleciona_cores', idioma)}**")
                cols = st.columns(len(spectra))
                custom_colors = []
                import plotly  # Certifique-se de que a biblioteca Plotly esteja importada
                for i, col in enumerate(cols):
                    with col:
                        default_color = plotly.colors.qualitative.Plotly[i % 10]
                        custom_colors.append(
                            st.color_picker(
                                f"{traduzir('cor', idioma)} {i+1}",
                                value=default_color,
                                key=f"spectrum_color_{i}"
                            )
                        )

                PRESETS = {
                    "color_theme": "plotly",
                    "template": "ggplot2",
                    "dash": dash_styles,
                    "linewidth": linewidth,
                    "mode": plot_mode,
                    "show_legend": show_legend,
                    "color": custom_colors
                }

                # Adicionando o spinner para indicar o processamento do gráfico
                with st.spinner(traduzir("gerando_grafico", idioma)):
                    fig = plot_combined_spectra(spectra, PRESETS)
                    fig.update_layout(
                        font=dict(family="Arial", size=12),
                        plot_bgcolor='white',
                        margin=dict(l=50, r=50, b=50, t=50),
                        xaxis=dict(showgrid=True, gridcolor='lightgray'),
                        yaxis=dict(showgrid=True, gridcolor='lightgray')
                    )
                    st.plotly_chart(fig, use_container_width=True)

                st.markdown(f"**{traduzir('arquivos_carregados', idioma)}**")
                for i, file in enumerate(uploaded_files, 1):
                    st.caption(f"{i}. {file.name}")
            else:
                st.info(traduzir("info_carregar_espectros", idioma))
        else:
            st.info(traduzir("info_carregar_espectros", idioma))
