import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Configuração
st.set_page_config(
    page_title="Qualidade do Ar no Brasil",
    layout="wide",
    page_icon="📊"
)

# Conexão com o banco
engine = create_engine("sqlite:///database/qualidade_ar_brasil.sqlite")

# Leitura dos dados
df = pd.read_sql("SELECT * FROM qualidade_ar", engine)

# Sidebar - Filtros
st.sidebar.header("Filtros")

# Filtro de região

regioes = sorted(df["regiao"].unique())

regiao_selecionada = st.sidebar.multiselect(
    "Seleção por região",
    regioes
)

# Filtra temporariamente pela região escolhida
df_temp = df.copy()

if regiao_selecionada:
    df_temp = df_temp[
        df_temp["regiao"].isin(regiao_selecionada)
    ]

# Filtro de estado


estados = sorted(df_temp["uf"].unique())

estado_selecionado = st.sidebar.multiselect(
    "Seleção por estado",
    estados
)

# Filtra temporariamente pelos estados escolhidos
if estado_selecionado:
    df_temp = df_temp[
        df_temp["uf"].isin(estado_selecionado)
    ]

# Filtro de cidade

cidades = sorted(df_temp["cidade"].unique())

cidade_selecionada = st.sidebar.multiselect(
    "Seleção por cidade",
    cidades
)

# Filtro de ano

anos = sorted(df["ano"].unique())

ano_selecionado = st.sidebar.multiselect(
    "Seleção por ano",
    anos
)

# Filtro de período

df["ano_mes"] = pd.to_datetime(df["ano_mes"])

data_min = df["ano_mes"].min().date()
data_max = df["ano_mes"].max().date()

periodo = st.sidebar.date_input(
    "Período",
    value=(data_min, data_max),
    min_value=data_min,
    max_value=data_max
)

# Aplicação dos filtros

df_filtro = df.copy()

if regiao_selecionada:
    df_filtro = df_filtro[
        df_filtro["regiao"].isin(regiao_selecionada)
    ]

if estado_selecionado:
    df_filtro = df_filtro[
        df_filtro["uf"].isin(estado_selecionado)
    ]

if cidade_selecionada:
    df_filtro = df_filtro[
        df_filtro["cidade"].isin(cidade_selecionada)
    ]

if ano_selecionado:
    df_filtro = df_filtro[
        df_filtro["ano"].isin(ano_selecionado)
    ]

if len(periodo) == 2:
    df_filtro = df_filtro[
        (df_filtro["ano_mes"].dt.date >= periodo[0]) &
        (df_filtro["ano_mes"].dt.date <= periodo[1])
    ]

# Título e KPIs

st.title("Análise da Qualidade do Ar no Brasil")

st.write("Dashboard de análise dos dados de qualidade do ar em cidades do Brasil entre 2015 e 2024.")

st.write("Aluno: Davi Cavalcante Rodrigues Scarpelli ")
    
st.write("Professor: Alexandre Neves Louzada") 

indice_medio = df_filtro["indice_qualidade_ar"].mean()

cidade_mais_afetada = (
    df_filtro.groupby("cidade")["indice_qualidade_ar"]
    .mean()
    .idxmax()
)

regiao_mais_afetada = (
    df_filtro.groupby("regiao")["indice_qualidade_ar"]
    .mean()
    .idxmax()
)

poluentes = ["pm25", "pm10", "no2", "co", "o3"]

poluente_predominante = (
    df_filtro[poluentes]
    .mean()
    .idxmax()
)

media_pm25 = df_filtro["pm25"].mean()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Índice Médio",
        f"{indice_medio:.2f}"
    )

with col2:
    st.metric(
        "Cidade Mais Afetada",
        cidade_mais_afetada
    )

with col3:
    st.metric(
        "Região Mais Afetada",
        regiao_mais_afetada
    )

with col4:
    st.metric(
        "Poluente Predominante",
        poluente_predominante.upper()
    )

with col5:
    st.metric(
        "Média de PM 2.5",
        f"{media_pm25:.2f}"
    )

aba1, aba2, aba3, aba4, aba5 = st.tabs([
    "Visão Geral",
    "Análise por ocorrências críticas",
    "Comparação geográfica",
    "Análise de poluentes",
    "Dados"
])

# Graficos

# Linha 1: Evolução temporal por mês

with aba1:

    st.subheader("Significado dos poluentes")

    poluentes_info = pd.DataFrame({
        "Sigla": ["PM2.5", "PM10", "NO₂", "CO", "O₃"],
        "Significado": [
            "Material particulado fino",
            "Material particulado inalável",
            "Dióxido de nitrogênio",
            "Monóxido de carbono",
            "Ozônio"
        ]
    })

    st.table(poluentes_info)

    st.subheader("Evolução Mensal da Qualidade do Ar")

    qualidade_por_mes = (
        df_filtro.groupby("ano_mes")["indice_qualidade_ar"]
        .mean()
        .reset_index()
        .sort_values("ano_mes")
    )

    fig = px.line(
        qualidade_por_mes,
        x="ano_mes",
        y="indice_qualidade_ar",
        markers=True,
    )

    fig.update_layout(
        xaxis_title="Período",
        yaxis_title="Índice Médio de Qualidade do Ar"
    )

    fig.update_xaxes(
        range=[
            qualidade_por_mes["ano_mes"].min(),
            qualidade_por_mes["ano_mes"].max()
        ],
        dtick="M6",
        tickformat="%b/%Y"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success("Esse gráfico mostra a evolução mensal do índice médio de qualidade do ar nas cidades observadas, permitindo identificar períodos de maior e menor índice de poluição.")

    # Grafico de distribuição dos níveis de qualidade

    distribuicao_qualidade = (
        df_filtro["nivel_qualidade"]
        .value_counts()
        .reset_index()
    )

    distribuicao_qualidade.columns = ["nivel_qualidade", "ocorrencias"]

    fig = px.bar(
        distribuicao_qualidade,
        x="nivel_qualidade",
        y="ocorrencias",
        text="ocorrencias"
    )

    fig.update_layout(
        xaxis_title="Nível de qualidade",
        yaxis_title="Número de ocorrências"
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_container_width=True)

# Linha 2: Cidades com mais ocorrências de períodos críticos

with aba2:

    st.subheader("Cidades com mais ocorrencias de qualidade do ar em estado crítico")

    cidades_criticas = (
        df_filtro[df_filtro["nivel_qualidade"] == "Ruim"]
        .groupby("cidade")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    cidades_criticas.sort_values().plot(kind="barh", ax=ax)

    ax.set_title("10 Cidades com Mais Períodos de Qualidade do Ar Ruim", fontweight="bold", fontsize=12)
    ax.set_xlabel("Quantidade de períodos")
    ax.set_ylabel("Cidade")

    x = cidades_criticas.sort_values().plot(kind="barh")

    for i, valor in enumerate(cidades_criticas.sort_values()):
        x.text(valor + 0.1, i, f"{valor}", va="center", fontsize=10)

    st.pyplot(fig)

    st.info("A partir desse gráfico podemos realizar uma análise com base nas ocorrências críticas de poluição do ar registradas durante o período")

# Linha 3

with aba3:

    st.subheader("Comparação entre cidades")

    cidades_comparacao = st.multiselect(
        "Selecione cidades para comparar",
        sorted(df_filtro["cidade"].unique())
    )

    df_comparacao = df_filtro[
        df_filtro["cidade"].isin(cidades_comparacao)
    ]

    comparacao = (
        df_comparacao
        .groupby(["ano", "cidade"])["indice_qualidade_ar"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        comparacao,
        x="ano",
        y="indice_qualidade_ar",
        color="cidade",
        markers=True
    )

    fig.update_layout(
        xaxis_title="Ano",
        yaxis_title="Índice Médio de Qualidade do Ar"
    )

    fig.update_xaxes(dtick=1)

    st.plotly_chart(fig, use_container_width=True)

    st.info("Esse gráfico nos permite selecionar cidades específicas e comparar a sua evolução")

with aba4:

    # Evolução por poluente

    st.subheader("Evolução por poluente")

    poluente = st.selectbox(
        "Selecione o poluente",
        ["pm25", "pm10", "no2", "co", "o3"]
    )

    poluente_ano = (
        df_filtro.groupby("ano")[poluente]
        .mean()
        .reset_index()
    )

    fig = px.line(
        poluente_ano,
        x="ano",
        y=poluente,
        markers=True,
        title=f"Evolução do {poluente.upper()}"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("É possível selecionar de forma individual cada poluente e observar sua evolução")

    # Gráfico de correlação entre variáveis

    st.subheader("Correlação entre variáveis")

    variaveis = [
        "pm25", "pm10", "no2", "co", "o3",
        "temperatura_media", "umidade",
        "indice_qualidade_ar"
    ]

    correlacao = df_filtro[variaveis].corr()

    fig, ax = plt.subplots(figsize=(10, 7))

    sns.heatmap(
        correlacao,
        annot=True,
        fmt=".2f",
        ax=ax
    )

    st.pyplot(fig)

    st.warning("A partir desse gráfico de correlação, é possível notar que existe uma correlação alta entre o indíce de qualidade do ar e a presença de PM25 na atmosfera. Entretanto, não é possível observar uma correlação significativa entre o índice e a temperatura média ou umidade")


with aba5:

    st.subheader("Base de dados utilizada")

    st.download_button(
        label="Baixar CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="qualidade_ar_brasil.csv",
        mime="text/csv"
    )

    st.dataframe(df_filtro, use_container_width=True)

st.divider()
st.subheader("Conclusão executiva")
st.write("""
A análise permite identificar quais regiões, estados e cidades possuem os índices de poluição mais preocupantes. O dashboard transforma os dados de qualidade do ar em um sistema de apoio à tomada de decisão, permitindo que órgãos responsáveis possam observar e entender quais lugares devem receber mais atenção no combate à poluição da atmosfera
Professor: Alexandre Neves Louzada
""")   