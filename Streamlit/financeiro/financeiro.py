import streamlit as st
import plotly.express as px
from preparacoes.preparacao import prepare_payment_data, prepare_subscription_growth_data

def build_page(is_chosen: bool):
    if not is_chosen:
        return

    st.title("Análise Financeira dos Pagamentos")
    
    # Preparar dados financeiros
    data = prepare_payment_data()
    
    # Exibir métricas de faturamento total e reembolsos
    st.metric(label="Faturamento Total", value=f"R$ {data['total_successful_amount']:,.2f}")
    st.metric(label="Total de Reembolsos", value=f"R$ {data['total_failed_amount']:,.2f}")

    # Gráfico de Faturamento Mensal
    fig_monthly_revenue = px.line(data['monthly_revenue'], x='Month', y='Amount', title="Faturamento Mensal")
    st.plotly_chart(fig_monthly_revenue)

    # Gráfico de Pizza para Taxa de Sucesso e Falha dos Pagamentos
    fig_status = px.pie(data['status_counts'], values='Count', names='Status', title="Taxa de Sucesso e Falha dos Pagamentos")
    st.plotly_chart(fig_status)

    # Gráfico de Barras para Razões de Declínio
    fig_decline_reasons = px.bar(data['decline_reasons'], x='Decline Reason', y='Count', title="Razões de Declínio dos Pagamentos")
    st.plotly_chart(fig_decline_reasons)
    
    # Preparar dados de crescimento de assinantes
    subscribers_growth = prepare_subscription_growth_data()
    
    # Gráfico de Crescimento de Assinantes
    fig_subscribers_growth = px.line(
        subscribers_growth, x='Created (UTC)', y='Active Subscribers', title="Crescimento de Assinantes ao Longo do Tempo"
    )
    st.plotly_chart(fig_subscribers_growth)
