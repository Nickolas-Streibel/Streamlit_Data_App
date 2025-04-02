# 📡 MEIS AND DMEIS DATA APP STREAMLIT



---

## 📋 Índice

- [📖 Descrição do Projeto](#-descrição-do-projeto)
- [✔️ Status do Projeto](#️-status-do-projeto)
- [📚 O que é MEIS e DMEIS?](📚-O-que-é-MEIS-e-DMEIS?)
- [🔨 Funcionalidades](#-funcionalidades-do-projeto)
- [📁 Acesso ao Projeto](#-acesso-ao-projeto)
- [🛠️ Como Abrir e Rodar o Projeto](#️-como-abrir-e-rodar-o-projeto)
- [🚀 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [👨‍💻 Autor e Orientador](#-autor-e-orientador)

---

## 📖 Descrição do Projeto

Este projeto faz parte de uma iniciação cientifica feita por mim na Universidade Federal de Ciencias da Saúde de Porto Alegre. O intuito do desenvolvimento consiste em auxiliar na análise de dados relacionados ao **MEIS (Medium Energy Ion Scattering)** e **DMEIS (Differential Medium Energy Ion Scattering)**. O objetivo é criar uma interface interativa em **Streamlit** que permita:

- Carregar e processar dados experimentais.
- Visualizar gráficos gerados a partir dos espectros de espalhamento.
- Facilitar a interpretação dos resultados por meio de ferramentas computacionais intuitivas.

---

## ✔️ Status do Projeto

\:construction: **Projeto em fase de conclusão** \:construction:

---

## 🔨 Funcionalidades do Projeto

- **Upload de arquivos**: Permite ao usuário carregar arquivos contendo dados experimentais realizado em MEIS.
- **Geração de espectros**: Produz gráficos baseados nos dados inseridos, realizando a soma dos scans para MEIS e ainda o rebine para o DMEIS.
- **Processamento dos dados**: Realiza cálculos e transformações necessárias para a análise do MEIS e DMEIS, além disso permite observar algumas métricas de estatisca dos dados e ainda comparar varios espectros com a biblioteca Plotly.
- **Exportação de resultados**: Permite salvar os gráficos e arquivos processados para referência futura.

---

## 📁 Acesso ao Projeto

Você pode acessar o código do projeto ou [baixá-lo aqui](https://github.com/Nickolas-Streibel/MEIS-AND-DMEIS-DATA-APP-STREAMLIT-/archive/refs/heads/master.zip).

---

## 🛠️ Como Abrir e Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/Nickolas-Streibel/MEIS-AND-DMEIS-DATA-APP-STREAMLIT-.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd MEIS-AND-DMEIS-DATA-APP-STREAMLIT-
   ```
3. Crie um ambiente virtual e ative-o: (OPCIONAL)
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute o app:
   ```bash
   streamlit run app.py
   ```

O projeto também esta disponivel no própio sistema de deploy do Streamlit. Você pode acessa-lo [clicando aqui]().


---

## 🚀 Tecnologias Utilizadas

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly**
- **Matplotlib**

---

## 📚 O que é MEIS e DMEIS?

- **MEIS (Medium Energy Ion Scattering)**: É uma técnica utilizada para estudar a estrutura e composição de superfícies sólidas através do espalhamento de íons de energia média. Essa técnica é muito importante para algumas análises de perfil elementar dentro de áreas com microeletronica, tecnologia de sensores ou paineis solares, e claro, tem um papel fundamnetal dentro da Física médica nuclear ao estudar os efeitos das nanoparticulas quando relacionadas ao dano de tecido tumoral. (Tudo isso com precisão na escala ângstroms (Å))
- **DMEIS (Differential Medium Energy Ion Scattering)**: É uma variação do MEIS que fornece informações diferenciais sobre a distribuição dos elementos na superfície analisada, sendo assim, o DMEIS ajuda que seja mais facil interpretar o MEIS em profundidade, pois ele pega a soma dos scans e retorna um espectro.

Essas técnicas são amplamente utilizadas na física de superfícies e na análise de materiais.

---

## 👨‍💻 Autor e Orientador

| [<img src="https://avatars.githubusercontent.com/u/195215720?s=400&u=f536b6f2f37ec4af893cb10f0f872ee9588ff606&v=4" width=115><br><sub>Nickolas Streibel</sub>](https://github.com/Nickolas-Streibel) | [<img src="https://media.licdn.com/dms/image/v2/C4D03AQG01lO5W9ZJRA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1556927051753?e=1749081600&v=beta&t=C6zT_-OdP4TkeApMmo3uvJU0GXLU_Xpt7HS2clME1Fk" width=115><br><sub>Henrique Trombini</sub>](https://www.linkedin.com/in/henrique-trombini-6b780493/) |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Desenvolvedor** | **Orientador** |

---

