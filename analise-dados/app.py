import streamlit as st
import pandas as pd
import plotly.express as px

#Criação do Titulo
st.title("Dashboard de Desempenho de Alunos")

#Carregamento dos Dados
df = pd.read_csv("dados.csv")
st.subheader("Tabela de Dados")
st.dataframe(df)

#Criação de Filtros
curso = st.selectbox("Selecione o Curso",df["Curso"].unique())
df_filtado = df[df["Curso"] == curso]
st.write(df_filtado)

#Elaboração de Grafico

barra = px.bar(
        df_filtado,
        x="Aluno",
        y="Nota",
        color="Aluno",
        title="Notas dos Aulons"


)

st.plotly_chart(barra)