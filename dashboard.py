import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_excel('planilha.xlsx')
df2 = pd.read_excel('planilhaTeste.xlsx')
df1 = df['Ganhador 1'].sum(), df['Ganhador 2'].sum()
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)
cores = ['#FF5733', '#33FF57']
fig_vitorias = px.bar(df, y=['Ganhador 1', 'Ganhador 2'], color_discrete_map={'Ganhador 1': 'blue', 'Ganhador 2': 'green'}, title='total', barmode="group")
col1.plotly_chart(fig_vitorias)

#soma_coluna = df['Ganhador 2'].sum()
#fig_kind = px.pie(df2, values='Soma Ganhador 2', names='Soma Ganhador 2', title='total', color_discrete_sequence=cores)

#col2.plotly_chart(fig_kind)

#df_melted = pd.melt(df2, id_vars=['Resultado'], value_vars=['Soma Ganhador 1', 'Soma Ganhador 2'], var_name='Ganhador 1', value_name='Ganhador 2')

# Criar o gráfico de barras
#fig = px.bar(df_melted, x='Resultado', y='Ganhador 1', color='Ganhador 2', barmode='group', title='Gráfico de Barras')

# Exibir o gráfico
#col3.plotly_chart(fig)
