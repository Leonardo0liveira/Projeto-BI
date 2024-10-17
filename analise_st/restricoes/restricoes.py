# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import matplotlib.pyplot as plt

# def build_page(is_chosen: bool, base: pd.DataFrame):
#     st.title("Análise de Restrições e Dietas Alimentares")
    
#     custom_color = ['#5E498A']  # Cor personalizada
    
#     restricoes = ['restricao_lactose', 'restricao_gluten', 'restricao_soja', 
#                   'restricao_ovo', 'restricao_amendoim', 'vegetarianismo', 
#                   'veganismo', 'sem_restricao']
    
#     # Somar os valores de cada coluna para obter a frequência
#     restricoes_df = base[restricoes].sum()
#     restricoes_df.columns = ['Restrição', 'Frequência']
    
#     st.subheader("Distribuição de Restrições Alimentares")
#     fig = px.bar(restricoes_df, x='Restrição', y='Frequência',
#                  title='Restrições Alimentares dos Clientes',
#                  labels={'Restrição': 'Restrição', 'Frequência': 'Número de Clientes'},
#                  color_discrete_sequence=custom_color)
#     st.plotly_chart(fig)