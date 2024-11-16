import pandas as pd
import json
from datetime import datetime
import streamlit as st
import sqlite3

# Função para carregar e preparar a base principal de gostos dos clientes
def prepare_client_data():
    db_path = '/Users/leonardooliveira/Desktop/PBI-EXAI/Projeto-BI/DADOS PROJETO BI/Experimentai.db'
    conn = sqlite3.connect(db_path)

    # Leitura das tabelas do banco de dados
    df_gosto = pd.read_sql_query("SELECT * FROM DimGostoBaseNova;", conn)
    df_demografico = pd.read_sql_query("SELECT * FROM DimDemograficoBaseNova;", conn)
    df_cliente_fato = pd.read_sql_query("SELECT * FROM clienteFato;", conn)

    # Fechar a conexão com o banco de dados
    conn.close()

    # Fazer o merge usando outer join para incluir todas as linhas
    base = pd.merge(df_cliente_fato, df_gosto, on='id_gosto', how='inner')
    base = pd.merge(base, df_demografico, on='id_demografico', how='inner')
    
    return base

def prepare_subscription_growth_data():
    db_path = '/Users/leonardooliveira/Desktop/PBI-EXAI/Projeto-BI/DADOS PROJETO BI/Experimentai.db'
    conn = sqlite3.connect(db_path)
    
    # Carregar os dados de assinaturas ativas e canceladas
    active_subscriptions = pd.read_csv('/Users/leonardooliveira/Desktop/PBI-EXAI/Projeto-BI/DADOS PROJETO BI/subscriptions (30).csv', sep=",")
    canceled_subscriptions = pd.read_csv('/Users/leonardooliveira/Desktop/PBI-EXAI/Projeto-BI/DADOS PROJETO BI/subscriptions (31).csv', sep=",")
    
    # Converter colunas de data para datetime
    active_subscriptions['Created (UTC)'] = pd.to_datetime(active_subscriptions['Created (UTC)'])
    canceled_subscriptions['Created (UTC)'] = pd.to_datetime(canceled_subscriptions['Created (UTC)'])
    canceled_subscriptions['Canceled At (UTC)'] = pd.to_datetime(canceled_subscriptions['Canceled At (UTC)'])
    
    # Criar DataFrames para eventos de assinatura
    active_events = active_subscriptions[['Created (UTC)']].copy()
    active_events['Event'] = 1  # +1 para cada nova assinatura

    canceled_events = canceled_subscriptions[['Created (UTC)', 'Canceled At (UTC)']].copy()
    canceled_events['Event'] = 1  # +1 para cada início de assinatura
    canceled_events_canceled = canceled_events[['Canceled At (UTC)', 'Event']].copy()
    canceled_events_canceled.columns = ['Created (UTC)', 'Event']
    canceled_events_canceled['Event'] = -1  # -1 para cada cancelamento

    # Concatenar todos os eventos e ordenar por data
    all_events = pd.concat([active_events, canceled_events[['Created (UTC)', 'Event']], canceled_events_canceled])
    all_events = all_events.sort_values(by='Created (UTC)').reset_index(drop=True)
    
    # Filtrar para a data de início desejada (2023-11-02) e calcular o total acumulado de assinantes ativos
    start_date = '2023-11-02'
    all_events = all_events[all_events['Created (UTC)'] >= start_date]
    all_events['Active Subscribers'] = all_events['Event'].cumsum()
    
    return all_events

def prepare_payment_data():
    db_path = '/Users/leonardooliveira/Desktop/PBI-EXAI/Projeto-BI/DADOS PROJETO BI/Experimentai.db'
    conn = sqlite3.connect(db_path)
    
    financial_data = pd.read_sql_query("SELECT * FROM Pagamentos", conn)
    
    financial_data['Created date (UTC)'] = pd.to_datetime(financial_data['Created date (UTC)'], errors='coerce')
    financial_data['Amount'] = pd.to_numeric(financial_data['Amount'], errors='coerce')
    financial_data['Amount Refunded'] = pd.to_numeric(financial_data['Amount Refunded'], errors='coerce')
    
    conn.close()

    successful_payments = financial_data[financial_data['Status'] == 'Paid']
    failed_payments = financial_data[financial_data['Status'] == 'Failed']
    
    total_successful_amount = successful_payments['Amount'].sum()
    
    total_refunded_amount = financial_data['Amount Refunded'].sum()

    successful_payments['Month'] = successful_payments['Created date (UTC)'].dt.to_period('M')
    monthly_revenue = successful_payments.groupby('Month')['Amount'].sum().reset_index()
    monthly_revenue['Month'] = monthly_revenue['Month'].dt.strftime('%Y-%m')  # Formatar para exibição

    decline_reasons = failed_payments['Decline Reason'].value_counts().reset_index()
    decline_reasons.columns = ['Decline Reason', 'Count']

    status_counts = financial_data['Status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']

    return {
        "total_successful_amount": total_successful_amount,
        "total_failed_amount": total_refunded_amount,  # Usar `Amount Refunded` para reembolsos
        "monthly_revenue": monthly_revenue,
        "status_counts": status_counts,
        "decline_reasons": decline_reasons
    }
