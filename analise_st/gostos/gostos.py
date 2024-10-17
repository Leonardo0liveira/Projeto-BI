import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def build_page(is_chosen: bool, base: pd.DataFrame):
    st.title("Analise dos gostos dos clientes")
    
    st.dataframe(base.head(5))
    
    # Definindo a cor personalizada para os gráficos de barras
    custom_color = ['#5E498A']  # Cor hexadecimal correspondente a R:94, G:73, B:138

    # Definindo as cores específicas para os gráficos de pizza
    pie_colors = ['#5E498A', '#4B3A75', '#392B61', '#271C4D']
    
    # Análise: Você gosta de moda?
    st.subheader("Distribuição: Você gosta de moda?")
    frq_gostaModa = base['gosta_moda'].value_counts().reset_index()
    frq_gostaModa.columns = ['Resposta', 'Frequência']
    fig = px.bar(frq_gostaModa, x='Resposta', y='Frequência',
                 title='Frequência de resposta para "Você gosta de moda?"',
                 labels={'Resposta':'Resposta', 'Frequência':'Número de clientes'},
                 color_discrete_sequence=custom_color)
    st.plotly_chart(fig)
    
    # Análise: Você gosta de decoração?
    st.subheader("Distribuição: Você gosta de decoração?")
    frq_gostaDecoracao = base['gosta_decoracao'].value_counts().reset_index()
    frq_gostaDecoracao.columns = ['Resposta', 'Frequência']
    fig = px.pie(frq_gostaDecoracao, values='Frequência', names='Resposta',
                 title='Frequência de resposta para "Você gosta de decoração?"',
                 hole=0.4,
                 color_discrete_sequence=pie_colors[:len(frq_gostaDecoracao)])
    st.plotly_chart(fig)
    
    # Análise: Você consome alimentos saudáveis com frequência?
    st.subheader("Distribuição: Você consome alimentos saudáveis com frequência?")
    frq_consumeAlimentosSaudaveis = base['consome_alimentos_saudaveis'].value_counts().reset_index()
    frq_consumeAlimentosSaudaveis.columns = ['Resposta', 'Frequência']
    fig = px.bar(frq_consumeAlimentosSaudaveis, x='Resposta', y='Frequência',
                 title='Frequência de resposta para "Você consome alimentos saudáveis?"',
                 labels={'Resposta':'Resposta', 'Frequência':'Número de clientes'},
                 color_discrete_sequence=custom_color)
    st.plotly_chart(fig)
    
    # Análise: Você gosta de mexer com carros?
    st.subheader("Distribuição: Você gosta de mexer com carros?")
    frq_gostaCarros = base['gosta_carros'].value_counts().reset_index()
    frq_gostaCarros.columns = ['Resposta', 'Frequência']
    fig = px.pie(frq_gostaCarros, values='Frequência', names='Resposta',
                 title='Frequência de resposta para "Você gosta de mexer com carros?"',
                 hole=0.4,
                 color_discrete_sequence=pie_colors[:len(frq_gostaCarros)])
    st.plotly_chart(fig)
    
    ############################################################################
    ############################################################################
    st.subheader("Distribuição: Você gosta de moda?")
    frq_gostaModa = base['gosta_moda'].value_counts()
    fig, ax = plt.subplots()
    frq_gostaModa.plot(kind='bar', ax=ax)
    ax.set_title('Frequência de resposta para "Você gosta de moda?"')
    ax.set_xlabel('Resposta')
    ax.set_ylabel('Frequência')
    st.pyplot(fig)
    
    # Análise: Frequência de quem gosta de decoração
    st.subheader("Distribuição: Você gosta de decoração?")
    frq_gostaDecoracao = base['gosta_decoracao'].value_counts()
    fig, ax = plt.subplots()
    frq_gostaDecoracao.plot(kind='pie', ax=ax, )
    ax.set_title('Frequência de resposta para "Você gosta de decoração?"')
    ax.set_xlabel('Resposta')
    ax.set_ylabel('Frequência')
    st.pyplot(fig)
    
    # Análise: Frequência de quem consome alimentos saudáveis
    st.subheader("Distribuição: Você consome alimentos saudáveis com frequência?")
    frq_consumeAlimentosSaudaveis = base['consome_alimentos_saudaveis'].value_counts()
    fig, ax = plt.subplots()
    frq_consumeAlimentosSaudaveis.plot(kind='bar', ax=ax)
    ax.set_title('Frequência de resposta para "Você consome alimentos saudáveis?"')
    ax.set_xlabel('Resposta')
    ax.set_ylabel('Frequência')
    st.pyplot(fig)
    
    # Análise: Frequência de quem gosta de carros
    st.subheader("Distribuição: Você gosta de mexer com carros?")
    frq_gostaCarros = base['gosta_carros'].value_counts()
    fig, ax = plt.subplots()
    frq_gostaCarros.plot(kind='pie', ax=ax, autopct='%1.1f%%')
    ax.set_title('Frequência de resposta para "Você gosta de mexer com carros?"')
    ax.set_xlabel('Resposta')
    ax.set_ylabel('Frequência')
    st.pyplot(fig)