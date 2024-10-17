import streamlit as st
import pandas as pd

from preparacao.preparacao import prepare
import clientes.clientes as clientes_module
import gostos.gostos as gostos_module
import restricoes.restricoes as restricoes_module

def render_sidebar(base):
    st.sidebar.image('EAILogo.webp', width=150)   
    page = st.sidebar.selectbox("Análises",["Clientes", "Gostos", "Restrições"])
    
    if page == "Clientes":
        clientes_module.build_page(is_chosen=True, base=base)
        
    elif page == "Gostos":
        gostos_module.build_page(is_chosen=True , base=base)
     
    elif page == "Restrições":
        restricoes_module.build_page(is_chosen=True , base=base)
            
    st.session_state["selected_page"] = page

def main():
    st.title("Experimenta aí!")
        
    base = pd.read_csv('/Users/leonardooliveira/Desktop/PBI-EXAI/Projeto-BI/analise_st/responses.csv', sep=";")
    
    base = prepare(base)
    
    render_sidebar(base)
    
    duplicated_columns = base.columns[base.columns.duplicated()].tolist()
    if duplicated_columns:
        st.error(f"Colunas duplicadas encontradas: {duplicated_columns}")
    else:
        with st.toast("Sem colunas duplicadas detectadas!"):
            pass

if __name__ == '__main__':
    main()
