# plotting.py
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.colors
import streamlit as st


def plot_data(data_log, energy, theta, dtheta, traduzir):
    plot_width = 10
    plot_height = 6
    extent = [108, 132, energy[-1] - 1, energy[0]]
    vmin = np.min(data_log)
    vmax = np.max(data_log)

    fig, ax = plt.subplots(figsize=(plot_width, plot_height))
    ax.imshow(data_log, interpolation='gaussian', cmap='nipy_spectral_r',
              extent=extent, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    ax.set_ylabel(traduzir("Energy (keV)"))
    ax.set_xlabel(traduzir("Scattering angle (°)"))

    y_min = min(energy)
    y_max = max(energy)
    n_ticks = 10
    y_ticks = np.linspace(y_min, y_max, n_ticks)
    ax.set_yticks(y_ticks)

    ax.set_xticks(np.arange(110, 133, 2))
    plt.xticks(rotation=45)

    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)


def plot_spectrum_with_save(spec, traduzir):
    fig = go.Figure()
    for iAn in range(spec.angle_size):
        counts = [spec.counts[iEn][iAn] for iEn in range(spec.size)]
        fig.add_trace(go.Scatter(
            x=spec.energy,
            y=counts,
            mode='lines',
            name=f'{traduzir("angulo")} {iAn + 1}',
            hovertemplate="Energia: %{x:.2f} keV<br>Contagem: %{y:.2f}<extra></extra>"
        ))
    fig.update_layout(
        title=traduzir("titulo_grafico_meis"),
        xaxis_title=traduzir("energia") + " (keV)",
        yaxis_title=traduzir("contagem"),
        legend_title=traduzir("angulo"),
        hovermode='x unified',
        height=500
    )
    st.session_state['dmeis_plot'] = fig
    st.plotly_chart(fig)


def plot_combined_spectra(spectra, presets=None):

    if presets is None:
        presets = {}

    default_presets = {
        "linewidth": 2,
        "dash": ["solid"],  # Lista por padrão
        "mode": "lines",
        "show_legend": True,
        "template": "ggplot2",
        "color": ["#1f77b4", "#7f7f7f", "#000000", "#2ca02c", "#d62728"]
    }

    presets = {**default_presets, **presets}

    # Validação: se a lista de dash estiver vazia, lança erro
    if not presets["dash"]:
        raise ValueError("A lista de padrões de linha não pode estar vazia!")

    # Gerenciamento de cores: garantir que haja cores suficientes para todos os espectros
    colors = presets["color"]
    if len(colors) < len(spectra):
        colors = colors * (len(spectra) // len(colors) + 1)

    fig = go.Figure()

    for i, spectrum in enumerate(spectra):
        # Função auxiliar para ciclar parâmetros se forem listas
        def get_cycled(param):
            value = presets.get(param, default_presets[param])
            return value[i % len(value)] if isinstance(value, list) else value

        line_config = dict(
            width=get_cycled("linewidth"),
            dash=get_cycled("dash"),
            color=colors[i]
        )

        marker_config = None
        if "markers" in presets["mode"]:
            marker_config = dict(
                size=8,
                symbol="circle",
                color=colors[i]
            )

        fig.add_trace(go.Scatter(
            x=spectrum['energy'],
            y=spectrum['count'],
            mode=presets["mode"],
            name=f"Spectrum {i+1}",
            line=line_config,
            marker=marker_config
        ))

    fig.update_layout(
        title=presets.get("title", "Comparação de Espectros"),
        xaxis=dict(
            title={'text': presets.get("xaxis_title", "Energy (keV)"), 'font': {
                'color': "black"}},
            tickfont={'color': "black"},
            showgrid=True,
            gridcolor='lightgray'
        ),
        yaxis=dict(
            title={'text': presets.get("yaxis_title", "Counts"), 'font': {
                'color': "black"}},
            tickfont={'color': "black"},
            showgrid=True,
            gridcolor='lightgray'
        ),
        template=presets.get("template", "ggplot2"),
        showlegend=presets.get("show_legend", True),
        font=dict(
            family="Arial",
            size=12,
            color="black"
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(l=50, r=50, b=50, t=50),
        legend=dict(
            font=dict(color="black"),
            bgcolor="white",
            bordercolor="black",
            borderwidth=1
        )
    )

    return fig
