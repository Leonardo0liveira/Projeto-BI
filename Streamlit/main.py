import streamlit as st
import pandas as pd

# Importar módulos das diferentes páginas
import gostos.gostos as gostos_module
import clientes.clientes as clientes_module
import financeiro.financeiro as financeiro_module
# import possiveis_clientes.possiveis_clientes as possiveis_clientes_module
# import chat.chat as chat_module

from preparacoes.preparacao import prepare_client_data

def render_sidebar():
    # Exibir a imagem no sidebar
    st.sidebar.image('/Users/leonardooliveira/Desktop/PBI-EXAI/Projeto-BI/DADOS PROJETO BI/EAILogo.webp', width=150)  # Ajuste o caminho da imagem se necessário
    
    # Selecionar a página a ser exibida
    page = st.sidebar.selectbox("Análises", ["Gostos dos clientes", "Clientes", "Financeiro", "Possíveis clientes", "Chat"])
    
    # Atualizar a página selecionada no estado da sessão
    st.session_state["selected_page"] = page

def main():
    st.title("Experimentaí!")
    
    # Renderizar a sidebar e obter a página selecionada
    render_sidebar()
    selected_page = st.session_state["selected_page"]
    
    # Carregar dados conforme a página selecionada
    if selected_page == "Gostos dos clientes":
        # Carregar e processar a base de dados de gostos
        base_gostos = prepare_client_data()
        gostos_module.build_page(is_chosen=True, base=base_gostos)

    elif selected_page == "Clientes":
        base_clientes = prepare_client_data()
        clientes_module.build_page(is_chosen=True, base=base_clientes)
    
    elif selected_page == "Financeiro":
        # Carregar e processar a base de dados financeira
        financeiro_module.build_page(is_chosen=True)
        
    elif selected_page == "Chat":
        chat_module.build_chat_page(is_chosen=True)
    
    # elif selected_page == "Possíveis clientes":
    #     # Carregar e processar a base de dados de possíveis clientes
    #     base_possiveis_clientes = pd.read_csv('/caminho/para/arquivo_possiveis_clientes.csv', sep=";")  # Substitua pelo caminho correto
    #     possiveis_clientes_module.build_page(is_chosen=True, base=base_possiveis_clientes)
    
    # elif selected_page == "Chat":
    #     # Configurar a página de chat (sem necessidade de base de dados)
    #     chat_module.build_page(is_chosen=True)

if __name__ == '__main__':
    main()
