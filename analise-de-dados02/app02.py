import streamlit as st
import pandas as pd
import plotly.express as px

#Criação do Titulo
st.title("Dashboard de Funcionários")

#Carregamento dos Dados
df = pd.read_csv("novos_dados.csv")
st.subheader("Tabela de Dados")
st.dataframe(df)

#Criação de Filtros
depart = st.selectbox("Selecione o departamento",df["departamento"].unique())
df_filtado = df[df["d   1epartamento"] == depart]
st.write(df_filtado)

#Elaboração de Grafico

barra = px.bar(
        df_filtado,
        x="nome_completo",
        y="salario_mensal_brl",
        color="nome_completo",
        title="Funcionário"


)

st.plotly_chart(barra)