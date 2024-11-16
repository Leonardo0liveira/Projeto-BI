# import streamlit as st
# import sqlite3
# from langchain_community.agent_toolkits import create_sql_agent
# from langchain_openai import ChatOpenAI

# def build_chat_page(is_chosen: bool):
#     if not is_chosen:
#         return
    
#     # Título da página
#     st.title("Consultas Interativas com Agente SQL")
#     st.toast("Faça consultas ao banco de dados de forma interativa com o agente SQL!")

#     # Configuração do banco de dados
#     db_path = '/Users/leonardooliveira/Desktop/PBI-EXAI/Projeto-BI/DADOS PROJETO BI/Experimentai.db'
#     conn = sqlite3.connect(db_path)

#     # Função para criar e configurar o agente SQL
#     def create_sql_chat_agent(db_connection):
#         llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
#         agent_executor = create_sql_agent(
#             llm=llm,
#             db=db_connection,
#             agent_type="openai-tools",
#             verbose=True
#         )
#         return agent_executor

#     # Inicializar o histórico de chat no session_state, se ainda não estiver presente
#     if 'chat_history' not in st.session_state:
#         st.session_state.chat_history = []

#     # Criar o agente SQL
#     agent = create_sql_chat_agent(conn)

#     # Exibir o histórico de conversas usando os recursos de chat
#     st.subheader("Histórico de Conversas")
#     for message in st.session_state.chat_history:
#         if message['type'] == 'user':
#             with st.chat_message("user"):
#                 st.write(message['content'])
#         elif message['type'] == 'bot':
#             with st.chat_message("assistant"):
#                 st.write(message['content'])

#     # Input para a nova pergunta do usuário
#     user_question = st.chat_input("Digite sua pergunta... ")

#     # Processar a pergunta do usuário e exibir a resposta
#     if user_question:
#         # Armazenar a pergunta no histórico e exibi-la no chat
#         st.session_state.chat_history.append({"type": "user", "content": user_question})
#         with st.chat_message("user"):
#             st.write(user_question)

#         # Obter a resposta do agente SQL
#         response = agent.invoke(user_question)
        
#         # Armazenar a resposta no histórico e exibi-la no chat
#         st.session_state.chat_history.append({"type": "bot", "content": response})
#         with st.chat_message("assistant"):
#             st.write(response)

#     # Fechar a conexão com o banco de dados
#     conn.close()
