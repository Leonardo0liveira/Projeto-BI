import streamlit as st
import pandas as pd
import plotly.express as px

def build_page(is_chosen: bool, base: pd.DataFrame):
    if not is_chosen:
        return
    
    st.title("Análise descritiva do perfil pessoal dos clientes")
    
    st.toast("Selecione as categorias desejadas para análise e visualize os gráficos apropriados para cada uma.")
    
    # Exibir uma amostra dos dados
    st.dataframe(base.head(5))
    
    # Definindo a cor personalizada para os gráficos
    custom_color = ['#5E498A']  # Cor hexadecimal para gráfico de barras
    pie_colors = ['#5E498A', '#4B3A75', '#392B61', '#271C4D']  # Paleta para gráfico de pizza

    # Funções para criar gráficos
    def plot_bar_chart(column, title, top_n=10):
        data = base[column].value_counts().reset_index()
        data.columns = ['Resposta', 'Frequência']
        
        # Filtrar para mostrar apenas as principais categorias
        if len(data) > top_n:
            data_top = data.head(top_n)
            data_top.loc[top_n] = ['Outros', data['Frequência'][top_n:].sum()]
        else:
            data_top = data
        
        fig = px.bar(data_top, x='Resposta', y='Frequência',
                     title=title,
                     labels={'Resposta': 'Resposta', 'Frequência': 'Número de clientes'},
                     color_discrete_sequence=custom_color)
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig)

    def plot_pie_chart(column, title):
        data = base[column].value_counts().reset_index()
        data.columns = ['Resposta', 'Frequência']
        fig = px.pie(data, values='Frequência', names='Resposta',
                     title=title, hole=0.4,
                     color_discrete_sequence=pie_colors[:len(data)])
        st.plotly_chart(fig)

    def plot_histogram(column, title):
        fig = px.histogram(base, x=column, nbins=20, title=title)
        st.plotly_chart(fig)

    # Mapeamento de categorias e gráficos predefinidos
    bar_chart_columns = {
        "Renda": 'renda_id',
        "Faixa Etária": 'faixa_etaria',
        "Cidade": 'cidade',
        "Estado": 'estado',
        "Distribuicao de idade": 'idade'
    }
    
    pie_chart_columns = {
        "Gênero": 'genero',
        "Como Conheceu": 'como_conheceu',
        "Rede Social": 'rede_social',
        "Objetivo": 'objetivo_id'
    }
    
    # Multiselect para escolher as categorias
    st.subheader("Gráficos de Barras")
    selected_bar_categories = st.multiselect("Escolha as categorias para gráficos de barras", list(bar_chart_columns.keys()))
    for category in selected_bar_categories:
        column = bar_chart_columns[category]
        plot_bar_chart(column, f"Distribuição de {category}")

    st.subheader("Gráficos de Pizza")
    selected_pie_categories = st.multiselect("Escolha as categorias para gráficos de pizza", list(pie_chart_columns.keys()))
    for category in selected_pie_categories:
        column = pie_chart_columns[category]
        plot_pie_chart(column, f"Distribuição de {category}")

    

