import streamlit as st
import pandas as pd
import plotly.express as px

#Criação do Titulo
st.title("Dashboard de Desempenho de jogadores de times")

#Carregamento dos Dados
df = pd.read_csv("dados.csv")
st.subheader("Tabela de Dados")
st.dataframe(df)

#Criação de Filtros
time = st.selectbox("Selecione o time",df["Time"].unique())
df_filtado = df[df["Time"] == time]
st.write(df_filtado)

#Elaboração de Grafico

barra = px.bar(
        df_filtado,
        x="Jogador",
        y="Vitorias",
        color="Jogador",
        title="Jogadores:"


)

st.plotly_chart(barra)