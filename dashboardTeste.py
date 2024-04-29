import pandas as pd
import plotly.express as px

# Supondo que você tenha um DataFrame df com as colunas 'categoria', 'Ganhador 1' e 'Ganhador 2'
df = pd.DataFrame({
    'categoria': ['A', 'B', 'C', 'D'],
    'Ganhador 1': [10, 20, 30, 40],
    'Ganhador 2': [15, 25, 35, 45]
})

# Criar a primeira figura para 'Ganhador 1'
fig_vitorias_ganhador1 = px.bar(df, x='categoria', y='Ganhador 1', color='categoria', title='Ganhador 1', barmode="group")

# Criar a segunda figura para 'Ganhador 2'
fig_vitorias_ganhador2 = px.bar(df, x='categoria', y='Ganhador 2', color='categoria', title='Ganhador 2', barmode="group")

# Sobrepor as duas figuras
fig_vitorias_ganhador1.update_traces(marker=dict(color='blue'), selector=dict(type='bar'))
fig_vitorias_ganhador2.update_traces(marker=dict(color='green'), selector=dict(type='bar'))

# Exibir as figuras
fig_vitorias_ganhador1.show()
fig_vitorias_ganhador2.show()
