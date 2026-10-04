# Dashboard de Qualidade do Ar no Brasil

## 1. Descrição do projeto

Este projeto apresenta uma análise de dados sobre a **qualidade do ar em cidades brasileiras**, abrangendo diferentes regiões, estados e períodos.

O projeto foi desenvolvido como avaliação G1 da disciplina **Linguagem de Programação — Análise e Visualização de Dados com Python**.

O objetivo é transformar dados brutos de qualidade do ar em informações úteis para identificar **cidades, regiões, períodos e poluentes que merecem maior atenção**.

### Fluxo do projeto

```text
Dados brutos
    ↓
Tratamento e preparação (Pandas)
    ↓
Análise exploratória
    ↓
Persistência (SQLAlchemy + SQLite)
    ↓
Dashboard interativo (Streamlit)
    ↓
Visualizações e análise dos resultados
```

---

## 2. Problema de análise

A análise busca responder às seguintes perguntas:

- Quais cidades apresentam pior qualidade do ar?
- Existem períodos mais críticos?
- Quais poluentes apresentam maior presença nos dados?
- Existe relação entre clima e qualidade do ar?
- Há variação da qualidade do ar ao longo do tempo?
- Quais regiões apresentam maiores índices de poluição?
- Quais cidades exigem maior atenção ambiental?

---

## 3. Tecnologias utilizadas

| **Tecnologia** | **Função** |
|---|---|
| Python | Linguagem principal |
| pandas | Tratamento e análise dos dados |
| matplotlib | Visualização de dados |
| seaborn | Análise estatística e correlação |
| plotly | Visualizações interativas |
| SQLAlchemy | Conexão e persistência no banco |
| SQLite | Armazenamento dos dados |
| Streamlit | Desenvolvimento do dashboard |
| Git/GitHub | Versionamento e publicação |

---

## 4. Estrutura do projeto

```text
qualidade-ar-brasil/
|
|-- README.md
|-- requirements.txt
|-- app.py
|-- index.html
|
|-- dados/
|   |-- qualidade_ar_brasil.csv
|
|-- database/
|   |-- qualidade_ar_brasil.sqlite
|
|-- notebook/
|   |-- analise.ipynb
```

---

## 5. Como executar localmente

### 5.1 Clonar o repositório

```bash
git clone https://github.com/ScarpelliDavi/qualidade-ar-brasil.git
cd qualidade-ar-brasil
```

### 5.2 Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5.3 Executar o dashboard

```bash
streamlit run app.py
```

### 5.4 Executar o notebook

O notebook `analise.ipynb` pode ser aberto pelo **Jupyter Notebook**, **JupyterLab** ou **VS Code** e executado célula por célula.

---

## 6. Indicadores analisados

O projeto utiliza diferentes indicadores para avaliar a qualidade do ar, entre eles:

| **Indicador** | **Descrição** |
|---|---|
| Índice de Qualidade do Ar | Indicador geral da qualidade do ar |
| Nível de Qualidade | Classificação da qualidade do ar |
| PM2.5 | Concentração de partículas finas |
| PM10 | Concentração de partículas inaláveis |
| NO₂ | Concentração de dióxido de nitrogênio |
| CO | Concentração de monóxido de carbono |
| O₃ | Concentração de ozônio |
| Temperatura Média | Temperatura média registrada |
| Umidade | Umidade registrada |

---

## 7. Funcionalidades do dashboard

O dashboard desenvolvido em Streamlit apresenta:

- Filtros por região, estado e cidade
- Filtro por ano
- Filtro por período
- KPIs dinâmicos
- Evolução temporal do índice de qualidade do ar
- Distribuição dos níveis de qualidade
- Identificação das cidades com maior número de períodos críticos
- Comparação entre cidades
- Análise da evolução dos principais poluentes
- Matriz de correlação entre poluentes, clima e qualidade do ar
- Tabela interativa dos dados
- Download dos dados em formato CSV
- Conclusão executiva dos resultados

---

## 8. Análises realizadas

### 8.1 Análise temporal

Foi analisada a evolução do índice médio de qualidade do ar ao longo dos períodos disponíveis, permitindo identificar momentos de maior e menor concentração de poluição.

### 8.2 Análise de períodos críticos

Foram identificadas as cidades que apresentaram maior número de registros classificados como **"Ruim"**, permitindo destacar localidades que apresentaram maior frequência de períodos críticos.

### 8.3 Comparação entre cidades

O dashboard permite selecionar diferentes cidades e comparar a evolução do índice médio de qualidade do ar ao longo dos anos.

### 8.4 Análise dos poluentes

Foram analisados os principais poluentes presentes na base:

- PM2.5
- PM10
- NO₂
- CO
- O₃

A análise permite observar a evolução das concentrações e comparar o comportamento dos diferentes poluentes.

### 8.5 Análise de correlação

Foi construída uma matriz de correlação envolvendo os principais poluentes, o índice de qualidade do ar, temperatura média e umidade.

Essa análise permite identificar associações entre as variáveis presentes na base, sem estabelecer necessariamente relações de causa e efeito.

---

## 9. Principais resultados

A análise permite identificar:

- cidades com maior frequência de períodos classificados como críticos;
- regiões com maiores índices médios de qualidade do ar;
- variações da qualidade do ar ao longo do tempo;
- comportamento dos principais poluentes;
- possíveis relações entre qualidade do ar e variáveis climáticas.

Os resultados podem ser utilizados para direcionar análises mais específicas e identificar regiões e períodos que merecem maior atenção no monitoramento da qualidade do ar.

---

## 10. Banco de dados

Os dados tratados foram armazenados em um banco **SQLite**, utilizando **SQLAlchemy** para realizar a conexão entre o Python e o banco de dados.

O fluxo de persistência utilizado no projeto é:

```text
CSV
 ↓
Pandas
 ↓
Tratamento dos dados
 ↓
SQLite
 ↓
SQLAlchemy
 ↓
Streamlit
```

O banco permite que o dashboard carregue os dados de forma persistente, separando a etapa de armazenamento da etapa de visualização e análise.

---

### Links

**Repositório:**  
https://github.com/ScarpelliDavi/qualidade-ar-brasil.git

**Dashboard:**  
COLE-AQUI-O-LINK-DO-STREAMLIT

**GitHub Pages:**  
COLE-AQUI-O-LINK-DO-GITHUB-PAGES

---

## 11. Conclusão

A análise mostra como uma base de dados de qualidade do ar pode ser transformada em um produto analítico capaz de gerar informações relevantes para a tomada de decisão.

O projeto permite identificar:

- quais cidades apresentam maior frequência de períodos críticos;
- quais regiões apresentam os maiores índices de qualidade do ar;
- como a qualidade do ar varia ao longo do tempo;
- quais poluentes apresentam maior presença nos dados analisados;
- quais relações existem entre os poluentes, a qualidade do ar e as variáveis climáticas.

Essas informações podem auxiliar gestores e órgãos responsáveis pelo monitoramento ambiental a identificar regiões e períodos que exigem maior atenção, além de contribuir para o planejamento de ações de controle e redução da poluição atmosférica.

Aluno: Davi Cavalcante Rodrigues Scarpelli 
Professor: Alexandre Neves Louzada") 

---