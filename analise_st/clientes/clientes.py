import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def build_page(is_chosen: bool, base: pd.DataFrame):
    st.title("Análise dos nossos clientes")
    
    st.dataframe(base.head(5))
    
    # Definindo a cor personalizada para os gráficos de barras
    custom_color = ['#5E498A']  # Cor hexadecimal correspondente a R:94, G:73, B:138
    pie_colors = ['#5E498A', '#4B3A75', '#392B61', '#271C4D']

    # Análise: Proporção de clientes por estado
    st.subheader("Proporção de clientes por estado")
    frq_regiao = base['REGIAO'].value_counts().reset_index()
    frq_regiao.columns = ['Região', 'Frequência']
    fig = px.bar(frq_regiao, x='Região', y='Frequência', 
                 title="Distribuição de clientes por região",
                 labels={'Região':'Região', 'Frequência':'Número de clientes'},
                 color_discrete_sequence=custom_color)
    st.plotly_chart(fig)
    
    # Analise: distribuicao por genero
    st.subheader("Distribuição por Gênero")
    genero_counts = base['identificacao_genero'].value_counts().reset_index()
    genero_counts.columns = ['Gênero', 'Frequência']
    fig = px.pie(genero_counts, values='Frequência', names='Gênero',
                 title='Distribuição de Clientes por Gênero',
                 color_discrete_sequence=pie_colors[:len(genero_counts)])
    st.plotly_chart(fig)
    
    # Distribuição por faixa de renda
    st.subheader("Distribuição por Faixa de Renda")
    renda_counts = base['renda_mensal'].value_counts().reset_index()
    renda_counts.columns = ['Faixa de Renda', 'Frequência']
    fig = px.bar(renda_counts, x='Faixa de Renda', y='Frequência',
                 title='Distribuição de Clientes por Faixa de Renda',
                 labels={'Faixa de Renda': 'Faixa de Renda', 'Frequência': 'Número de Clientes'},
                 color_discrete_sequence=custom_color)
    st.plotly_chart(fig)
    
    st.subheader("Como os Clientes Conheceram a Empresa")
    origem_counts = base['como_conheceu'].value_counts().reset_index()
    origem_counts.columns = ['Origem', 'Frequência']
    fig = px.bar(origem_counts, x='Frequência', y='Origem', orientation='h',
                 title='Origem dos Clientes',
                 labels={'Frequência': 'Número de Clientes', 'Origem': 'Meio'},
                 color_discrete_sequence=custom_color)
    st.plotly_chart(fig)
    
    st.subheader("Locais Preferidos para Compra de Produtos de Beleza")
    locais_compra = base[''].value_counts().reset_index()
    locais_compra.columns = ['Local', 'Frequência']
    fig = px.bar(locais_compra, x='Frequência', y='Local', orientation='h',
                 title='Locais Preferidos de Compra',
                 labels={'Frequência': 'Número de Clientes', 'Local': 'Local de Compra'},
                 color_discrete_sequence=custom_color)
    st.plotly_chart(fig)
    
    # # Definindo as cores específicas para os gráficos de pizza
    # pie_colors = ['#5E498A', '#4B3A75', '#392B61', '#271C4D']

    #######################################################################################
    #######################################################################################
    
    # Análise: Proporção de clientes por região
    frq_regiao = base['REGIAO'].value_counts()
    fig, ax = plt.subplots()
    frq_regiao.plot(kind='bar', ax=ax)
    ax.set_title("Distribuição de clientes por região")
    ax.set_xlabel('Região')
    ax.set_ylabel('Frequência')
    st.pyplot(fig)
    
    # Análise: Distribuição de tipos de pele
    frq_tipoPele = base['tipo_pele'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(frq_tipoPele, labels=frq_tipoPele.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal') 
    st.pyplot(fig)
    
    # Análise: Frequência de quem usa maquiagem
    frq_usaMaquiagem = base['usa_maquiagem'].value_counts()
    fig, ax = plt.subplots()
    frq_usaMaquiagem.plot(kind='pie', ax=ax)
    ax.set_title('Frequência de resposta para "Você usa maquiagem?"')
    ax.set_xlabel('Resposta')
    ax.set_ylabel('Frequência')
    st.pyplot(fig)
    
    # Análise: Frequência de quem usa Cleanser
    frq_usoCleanser = base['uso_cleanser'].value_counts()
    fig, ax = plt.subplots()
    frq_usoCleanser.plot(kind='bar', ax=ax)
    ax.set_title('Frequência de resposta para "Você usa Cleanser?"')
    ax.set_xlabel('Resposta')
    ax.set_ylabel('Frequência')
    st.pyplot(fig)
    
    # Análise: Frequência de quem pratica esportes
    frq_praticaEsportes = base['pratica_esportes'].value_counts()
    fig, ax = plt.subplots()
    frq_praticaEsportes.plot(kind='bar', ax=ax)
    ax.set_title('Frequência de resposta para "Você pratica esportes?"')
    ax.set_xlabel('Resposta')
    ax.set_ylabel('Frequência')
    st.pyplot(fig)
    
    # Análise: Frequência de quem tem pet
    frq_temPet = base['tem_pet'].value_counts()
    fig, ax = plt.subplots()
    frq_temPet.plot(kind='bar', ax=ax)
    ax.set_title('Frequência de resposta para "Você tem um pet?"')
    ax.set_xlabel('Resposta')
    ax.set_ylabel('Frequência')
    st.pyplot(fig)
    
    
