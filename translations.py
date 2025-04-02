# translations.py

textos = {
    "titulo_app": {
        "pt": "Análise de Dados MEIS e DMEIS",
        "en": "MEIS and DMEIS Data Analysis"
    },
    "bem_vindo": {
        "pt": "Bem-vindo ao MEIS e DMEIS Data Analysis",
        "en": "Welcome to MEIS and DMEIS Data Analysis"
    },
    "nome_usuario": {
        "pt": "Digite seu nome:",
        "en": "Enter your name:"
    },
    "selecione_idioma": {
        "pt": "Selecione o idioma",
        "en": "Select the language"
    },
    "start": {
        "pt": "Iniciar",
        "en": "Start"
    },
    "erro_nome": {
        "pt": "Por favor, digite o seu nome.",
        "en": "Please enter your name."
    },
    "navegacao": {
        "pt": "Navegação",
        "en": "Navigation"
    },
    "inicio": {
        "pt": "🏠 Início",
        "en": "🏠 Home"
    },
    "instrucoes": {
        "pt": "📜 Instruções",
        "en": "📜 Instructions"
    },
    "meis": {
        "pt": "📊 MEIS",
        "en": "📊 MEIS"
    },
    "dmeis": {
        "pt": "📈 DMEIS",
        "en": "📈 DMEIS"
    },
    "feedback": {
        "pt": "📝 Feedback",
        "en": "📝 Feedback"
    },
    "descricao_inicio": {
        "pt": "Este aplicativo foi desenvolvido para auxiliar na análise de dados obtidos em experimentos de **MEIS** e **DMEIS**. Ele integra ferramentas interativas para o processamento e visualização dos dados, permitindo uma compreensão detalhada das propriedades de superfícies e camadas em materiais.\n\n### O que é MEIS?\n**MEIS (Medium Energy Ion Scattering)** é uma técnica que utiliza íons de energia média para investigar a estrutura de superfícies e interfaces com resolução atômica. É amplamente empregada em áreas como ciência dos materiais, física de superfícies e engenharia de semicondutores, fornecendo informações essenciais sobre a composição e o arranjo atômico da superfície.\n\n### O que é DMEIS?\n**DMEIS (Depth-resolved Medium Energy Ion Scattering)** é uma variação do MEIS que possibilita a análise da profundidade das camadas dos materiais. Ao ajustar parâmetros específicos, é possível obter um espectro que revela variações internas, auxiliando na determinação de espessuras e na identificação de gradientes de composição.\n\nUtilize as funcionalidades abaixo:\n- **Página MEIS:** Faça o upload dos seus arquivos de dados (formato `formatted.txt`) para gerar um gráfico de heatmap que consolida as informações experimentais.\n- **Página DMEIS:** Ajuste os parâmetros (como os limites inferiores e superiores dos ângulos, representados por amin e amax, e o bin de energia) para rebinar os dados e visualizar o espectro processado, podendo também fazer o download dos resultados.\n- **Página Feedback:** Envie suas sugestões e comentários para aprimorarmos o aplicativo.",
        "en": "This application was developed to assist in the analysis of data obtained from **MEIS** and **DMEIS** experiments. It integrates interactive tools for processing and visualizing data, providing a detailed understanding of surface and layer properties in materials.\n\n### What is MEIS?\n**MEIS (Medium Energy Ion Scattering)** is a technique that uses medium-energy ions to investigate surface and interface structures with atomic resolution. It is widely used in materials science, surface physics, and semiconductor engineering, offering essential information about the composition and atomic arrangement at the surface.\n\n### What is DMEIS?\n**DMEIS (Depth-resolved Medium Energy Ion Scattering)** is a variation of MEIS that enables the analysis of material layer depth. By adjusting specific parameters, you can obtain a spectrum that reveals internal variations, helping to determine layer thicknesses and identify composition gradients.\n\nUse the features below:\n- **MEIS Page:** Upload your data files (in `formatted.txt` format) to generate a heatmap graph that summarizes the experimental data.\n- **DMEIS Page:** Adjust parameters (such as the lower and upper angular limits, represented by amin and amax, and the energy bin) to rebin the data and view the processed spectrum, with the option to download the results.\n- **Feedback Page:** Submit your suggestions and comments so that we can improve the application."
    },
    "descricao_instrucoes": {
        "pt": "Para utilizar este aplicativo de forma eficaz, siga os passos abaixo:\n\n1. **Carregue os arquivos:** Acesse a página **MEIS** e faça o upload dos seus arquivos de dados no formato `formatted.txt`. Estes arquivos contêm os dados brutos dos experimentos.\n\n2. **Visualize os dados:** Após o upload, um gráfico de heatmap será gerado automaticamente, representando a distribuição das contagens em função da energia e dos ângulos medidos.\n\n3. **Realize a análise DMEIS:** Vá para a página **DMEIS** para ajustar os parâmetros de processamento. Aqui, você pode modificar os limites dos ângulos (utilizando os parâmetros amin e amax) e o bin de energia (denergy) para rebinar os dados e extrair o espectro desejado.\n\n4. **Baixe os resultados:** Assim que o gráfico for atualizado com os novos parâmetros, você poderá visualizar o espectro rebinado e fazer o download de um arquivo com os dados processados.\n\n5. **Feedback:** Se tiver dúvidas, sugestões ou encontrar algum problema, utilize a página **Feedback** para nos informar. Seu retorno é essencial para aprimorarmos o aplicativo.",
        "en": "To effectively use this application, follow the steps below:\n\n1. **Upload the files:** Go to the **MEIS** page and upload your data files in the `formatted.txt` format. These files contain the raw experimental data.\n\n2. **Visualize the data:** After uploading, a heatmap graph will be automatically generated, representing the distribution of counts as a function of the measured energy and angles.\n\n3. **Perform DMEIS analysis:** Navigate to the **DMEIS** page to adjust the processing parameters. Here, you can modify the angular limits (using the parameters amin and amax) and the energy bin (denergy) to rebin the data and extract the desired spectrum.\n\n4. **Download the results:** Once the graph is updated with the new parameters, you can view the rebinned spectrum and download a file with the processed data.\n\n5. **Feedback:** If you have questions, suggestions, or encounter any issues, use the **Feedback** page to let us know. Your feedback is essential for improving the application."
    },
    "descricao_feedback": {
        "pt": "Por favor, deixe seus comentários ou sugestões abaixo:",
        "en": "Please leave your comments or suggestions below:"
    },
    "mensagem_feedback": {
        "pt": "Você pode escrever seus comentários na caixa de texto abaixo",
        "en": "You can write your comments in the text box below"
    },
    "empty_feedback": {
        "pt": "Por favor, digite um feedback.",
        "en": "Please enter a feedback."
    },
    "enviar_feedback": {
        "pt": "Enviar",
        "en": "Submit"
    },
    "obrigado_feedback": {
        "pt": "Obrigado pelo seu feedback!",
        "en": "Thank you for your feedback!"
    },
    "creditos": {
        "pt": "Desenvolvido por: Nickolas Kaefer Streibel",
        "en": "Developed by: Nickolas Kaefer Streibel"
    },
    "reset_dmeis_help": {
        "pt": "Redefine todas as variáveis para os valores padrão.",
        "en": "Resets all variables to default values."
    },
    "Atualizar_grafico_help": {
        "pt": "Aperte para atualizar o gráfico com as variáveis alteradas",
        "en": "Press to update the graph with the changed variables"
    },
    "selecione_arquivos_meis": {
        "pt": "Selecione os arquivos formatted.txt",
        "en": "Select the formatted.txt files"
    },
    "visualizacao_grafico": {
        "pt": "Visualização do Gráfico",
        "en": "Graph Visualization"
    },
    "parametros_analise": {
        "pt": "Parâmetros de Análise",
        "en": "Analysis Parameters"
    },
    "escolha_arquivo_espectro": {
        "pt": "Escolha um arquivo de espectro",
        "en": "Choose a spectrum file"
    },
    "grafico_espectro_rebinado": {
        "pt": "Gráfico do Espectro Rebinado",
        "en": "Rebinned Spectrum Graph"
    },
    "ajuda_amin": {
        "pt": "Parâmetro amin: define o limite inferior do intervalo de ângulos considerado na análise. Ao alterá-lo, você filtra os dados para focar em uma faixa específica, podendo modificar o espectro resultante.",
        "en": "Parameter amin: sets the lower limit of the angular interval considered in the analysis. Changing this value filters the data to focus on a specific range, which may modify the resulting spectrum."
    },
    "ajuda_amax": {
        "pt": "Parâmetro amax: define o limite superior do intervalo de ângulos considerado na análise. Ao ajustá-lo, você controla quais dados são incluídos, podendo aumentar ou reduzir o ruído no espectro.",
        "en": "Parameter amax: sets the upper limit of the angular interval considered in the analysis. Adjusting this value controls which data are included, potentially increasing or reducing noise in the spectrum."
    },
    "ajuda_denergy": {
        "pt": "Parâmetro denergy: determina o tamanho do bin de energia para o espectro rebinado. Alterá-lo modifica a resolução do espectro, podendo torná-lo mais suave ou mais detalhado.",
        "en": "Parameter denergy: determines the bin size for the rebinned energy spectrum. Changing this value alters the resolution of the spectrum, making it smoother or more detailed."
    },
    "ajuda_angle_min": {
        "pt": "Parâmetro angle_min: indica o ângulo mínimo original do espectro, conforme medido nos dados. Geralmente, esse valor é fixo e alterar pode distorcer a escala dos ângulos.",
        "en": "Parameter angle_min: indicates the original minimum angle of the spectrum as measured in the data. This value is usually fixed, and changing it may distort the angular scale."
    },
    "ajuda_angle_bin_size": {
        "pt": "Parâmetro angle_bin_size: define o tamanho do bin de ângulos, isto é, o incremento entre os ângulos medidos. Modificar esse valor altera a granularidade da análise e a distribuição das contagens.",
        "en": "Parameter angle_bin_size: defines the bin size for angles, i.e., the increment between measured angles. Changing this value alters the granularity of the analysis and the distribution of counts."
    },
    "titulo_amin": {
        "pt": "Ângulo mínimo (amin)",
        "en": "Minimum angle (amin)"
    },
    "titulo_amax": {
        "pt": "Ângulo máximo (amax)",
        "en": "Maximum angle (amax)"
    },
    "titulo_denergy": {
        "pt": "Tamanho do bin de energia (d)",
        "en": "Energy bin size (d)"
    },
    "titulo_angle_min": {
        "pt": "Ângulo mínimo do espectro",
        "en": "Minimum spectrum angle"
    },
    "titulo_angle_bin_size": {
        "pt": "Tamanho do bin de ângulo",
        "en": "Angle bin size"
    },
    "energia_contagens_rebinadas": {
        "pt": "Energia e Contagens Rebinadas:",
        "en": "Rebinned Energy and Counts:"
    },
    "atualizar_grafico": {
        "pt": "Atualizar",
        "en": "Refresh"
    },
    "angulo": {
        "pt": "Ângulo",
        "en": "Angle"
    },
    "energia": {
        "pt": "Energia",
        "en": "Energy"
    },
    "contagem": {
        "pt": "Contagem",
        "en": "Counts"
    },
    "titulo_grafico_meis": {
        "pt": "Gráfico do Espectro MEIS",
        "en": "MEIS Spectrum Chart"
    },
    "reset_titulo": {
        "pt": "Resetar",
        "en": "Reset"
    },
    "valores_redefinidos": {
        "pt": "As variáveis foram redefinidas!",
        "en": "The variables have been redefined!"
    },
    "angle_min_menor_que_amax": {
        "pt": "Ajuste inválido! Para o espectro ser gerado, o ângulo mínimo precisa ser menor que o ângulo máximo",
        "en": "Invalid setting! The minimum angle must be smaller than the maximum angle"
    },
    "amax_maior_que_angle_min": {
        "pt": "Ajuste inválido! Para o espectro ser gerado, o ângulo mínimo precisa ser menor que o ângulo máximo",
        "en": "Invalid setting! The minimum angle must be smaller than the maximum angle"
    },
    "resumo_estatistico": {
        "pt": "Resumo Estatístico",
        "en": "Statistical Summary"
    },
    "average_counts_by_energy": {
        "pt": "Média das contagens por energia",
        "en": "Average counts by energy"
    },
    "no_summary_available": {
        "pt": "Nenhum resumo disponível. Atualize o gráfico para gerar o resumo.",
        "en": "No summary available. Update the chart to generate the summary."
    },
    "info": {
        "pt": "Configure os parâmetros e atualize o gráfico para visualizar os resultados.",
        "en": "Configure the parameters and update the graph to view the results."
    },
    "atualizacao_concluida": {
        "pt": "Gráfico atualizado!",
        "en": "Graph updated!"
    },
    "erro_arquivo_vazio": {
        "pt": "Arquivo vazio detectado!",
        "en": "Empty file detected!"
    },
    "erro_formato_arquivo": {
        "pt": "Formato de arquivo inválido. Esperado formato: 2 colunas numéricas.",
        "en": "Invalid file format. Expected format: 2 numeric columns."
    },
    "erro_tamanho_arquivos": {
        "pt": "Arquivos com tamanhos incompatíveis. Verifique os dados.",
        "en": "Files with incompatible sizes. Please check the data."
    },
    "erro_carregamento": {
        "pt": "Erro ao carregar arquivos",
        "en": "Error loading files"
    },
    "erro_arquivo_curto": {
        "pt": "Arquivo muito curto. Verifique o conteúdo.",
        "en": "File too short. Please check the content."
    },
    "erro_colunas": {
        "pt": "Número de colunas inválido. Verifique o formato do arquivo.",
        "en": "Invalid number of columns. Please check the file format."
    },
    "erro_valores_numericos": {
        "pt": "Valores não numéricos encontrados. Verifique os dados.",
        "en": "Non-numeric values found. Please check the data."
    },
    "erro_leitura_arquivo": {
        "pt": "Erro ao ler o arquivo",
        "en": "Error reading file"
    },
    "erro_inesperado": {
        "pt": "⚠️ Ocorreu um erro inesperado!",
        "en": "⚠️ An unexpected error occurred!"
    },
    "contate_suporte": {
        "pt": "Por favor, contate o suporte técnico.",
        "en": "Please contact technical support."
    },
    "reiniciar_aplicativo": {
        "pt": "🔄 Reiniciar Aplicativo",
        "en": "🔄 Restart App"
    },
    "erro_plotagem": {
        "pt": "Erro ao gerar o gráfico",
        "en": "Error generating the chart"
    },
    "gerando_grafico": {
        "pt": "Gerando gráfico...",
        "en": "Generating chart..."
    },
    "grafico_gerado": {
        "pt": "Gráfico gerado com sucesso!",
        "en": "Chart generated successfully!"
    },
    "dados_nao_carregados": {
        "pt": "Dados não carregados. Por favor, carregue os arquivos primeiro.",
        "en": "Data not loaded. Please upload the files first."
    },
    "intensidade": {
        "pt": "Intensidade (log)",
        "en": "Intensity (log)"
    },
    "muito_baixa": {
        "pt": "Muito Baixa",
        "en": "Very Low"
    },
    "baixa": {
        "pt": "Baixa",
        "en": "Low"
    },
    "media": {
        "pt": "Média",
        "en": "Medium"
    },
    "alta": {
        "pt": "Alta",
        "en": "High"
    },
    "muito_alta": {
        "pt": "Muito Alta",
        "en": "Very High"
    },
    "erro_sem_arquivo": {
        "pt": "Por favor, carregue um arquivo antes de atualizar o gráfico.",
        "en": "Please upload a file before updating the graph."
    },
    "comparacao_espectros": {
        "pt": "Comparação de Espectros",
        "en": "Spectrum Comparison"
    },
    "comparacao_espectros": {
        "pt": "Comparação de Espectros (Plotly)",
        "en": "Spectra Comparison (Plotly)"
    },
    "seleciona_espectros": {
        "pt": "Selecione os arquivos de spectrum para comparar",
        "en": "Select spectrum files to compare"
    },
    "erro_carregar_arquivo": {
        "pt": "Erro ao carregar o arquivo",
        "en": "Error loading file"
    },
    "configuracoes_visualizacao": {
        "pt": "Configurações de Visualização",
        "en": "Display Settings"
    },
    "largura_linha": {
        "pt": "Largura da Linha",
        "en": "Line Width"
    },
    "padrao_linhas": {
        "pt": "Padrão das Linhas (selecione pelo menos um)",
        "en": "Line Style (select at least one)"
    },
    "erro_selecao_linhas": {
        "pt": "Selecione pelo menos um estilo de linha!",
        "en": "Please select at least one line style!"
    },
    "modo_exibicao": {
        "pt": "Modo de Exibição",
        "en": "Display Mode"
    },
    "mostrar_legenda": {
        "pt": "Mostrar Legenda",
        "en": "Show Legend"
    },
    "seleciona_cores": {
        "pt": "Seleção de Cores por Espectro",
        "en": "Color Selection per Spectrum"
    },
    "cor": {
        "pt": "Cor",
        "en": "Color"
    },
    "arquivos_carregados": {
        "pt": "Arquivos carregados:",
        "en": "Uploaded files:"
    },
    "info_carregar_espectros": {
        "pt": "Carregue pelo menos um arquivo de spectrum para visualizar a comparação.",
        "en": "Upload at least one spectrum file to view the comparison."
    },
    "gerando_grafico": {
        "pt": "Gerando gráfico...",
        "en": "Generating graph..."
    }

}


def traduzir(chave, idioma="en"):
    return textos.get(chave, {}).get(idioma, chave)
