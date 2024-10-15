import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from prep.preparacao import prepare

def main():
    st.title("Analise de dados de clientes")
    
    base = pd.read_csv('/Users/leonardooliveira/Desktop/PBI/Projeto-BI/analise_st/responses.csv', sep=";")
    
    base= base.fillna(False)
    
    base = prepare(base)
    
    duplicated_columns = base.columns[base.columns.duplicated()].tolist()
    if duplicated_columns:
        st.error(f"Colunas duplicadas encontradas: {duplicated_columns}")
    else:
        with st.toast("Sem colunas duplicadas detectadas!"):
            pass
    
    st.dataframe(base.head(5))
    
    frq_gostaModa =                 base['gosta_moda'].value_counts()
    frq_pessoaArtistica =           base['pessoa_artistica'].value_counts()
    frq_usaMaquiagem =              base['usa_maquiagem'].value_counts()
    frq_usoTonico =                 base['uso_tonico'].value_counts()
    frq_usoCleanser =               base['uso_cleanser'].value_counts()
    frq_usoCleansingOil =           base['uso_cleansing_oil'].value_counts()
    frq_usoCremeOlhos =             base['uso_creme_olhos'].value_counts()
    frq_maquiagemOlhos =            base['maquiagem_olhos'].value_counts()
    frq_maquiagemLabios =           base['maquiagem_labios'].value_counts()
    frq_maquiagemRosto =            base['maquiagem_rosto'].value_counts()
    frq_usoEsmalte =                base['uso_esmalte'].value_counts()
    frq_usoMascaraFacial =          base['uso_mascara_facial'].value_counts()
    frq_usoMascaraCapilar =         base['uso_mascara_capilar'].value_counts()
    frq_usoProtetorSolar =          base['uso_protetor_solar'].value_counts()
    frq_usoProdutoModelarCabelo =   base['uso_produto_modelar_cabelo'].value_counts()
    frq_usoPerfume =                base['uso_perfume'].value_counts()
    frq_usoEsfolianteFacial =       base['uso_esfoliante_facial'].value_counts()
    frq_tratamentoManchasAcne =     base['tratamento_manchas_acne'].value_counts()
    frq_usoSerumOleo =              base['uso_serum_oleo'].value_counts()
    frq_usoRemovedorMaquiagem =     base['uso_removedor_maquiagem'].value_counts()
    frq_usoTopicosMedicados =       base['uso_topicos_medicados'].value_counts()
    frq_semRotinaBeleza =           base['sem_rotina_beleza'].value_counts()
    frq_ondeCompraProdutosBeleza =  base['onde_compra_produtos_beleza'].value_counts()
    frq_tipoPele =                  base['tipo_pele'].value_counts()
    frq_criterioCompraProduto =     base['criterio_compra_produto'].value_counts()
    frq_gostaBrinquedosJogos =      base['gosta_brinquedos_jogos'].value_counts()
    frq_praticaEsportes =           base['pratica_esportes'].value_counts()
    frq_temPet =                    base['tem_pet'].value_counts()
    frq_gostaDecoracao =            base['gosta_decoracao'].value_counts()
    frq_consumeAlimentosSaudaveis = base['consome_alimentos_saudaveis'].value_counts()
    frq_fanGastronomia =            base['fan_gastronomia'].value_counts()
    frq_gostaCarros =               base['gosta_carros'].value_counts()
    frq_recentementePaiMae =        base['recentemente_pai_mae'].value_counts()
    frq_gostaBebidasAlcoolicas =    base['gosta_bebidas_alcoolicas'].value_counts()
    frq_interesseCuidadosPessoais = base['interesse_cuidados_pessoais'].value_counts()
    frq_fanTecnologia =             base['fan_tecnologia'].value_counts()
    frq_criadorInfluencer =         base['criador_influencer'].value_counts()
    frq_interesseModa =             base['interesse_moda'].value_counts()
    frq_interesseArte =             base['interesse_arte'].value_counts()
    frq_interesseMaquiagem =        base['interesse_maquiagem'].value_counts()
    frq_interesseBrinquedosJogos =  base['interesse_brinquedos_jogos'].value_counts()
    frq_interesseEsportes =         base['interesse_esportes'].value_counts()
    frq_interessePets =             base['interesse_pets'].value_counts()
    frq_interesseDecoracao =        base['interesse_decoracao'].value_counts()
    frq_interesseBemEstar =         base['interesse_bem_estar'].value_counts()
    frq_interesseGastronomia =      base['interesse_gastronomia'].value_counts()
    frq_interesseCarros =           base['interesse_carros'].value_counts()
    frq_interesseParentalidade =    base['interesse_parentalidade'].value_counts()
    frq_interesseBebidas =          base['interesse_bebidas'].value_counts()
    frq_interesseCuidadosPessoais = base['interesse_cuidados_pessoais'].value_counts()
    frq_interesseTecnologia =       base['interesse_tecnologia'].value_counts()
    frq_restricaoLactose =          base['restricao_lactose'].value_counts()
    frq_restricaoGluten =           base['restricao_gluten'].value_counts()
    frq_restricaoSoja =             base['restricao_soja'].value_counts()
    frq_restricaoOvo =              base['restricao_ovo'].value_counts()
    frq_restricaoAmendoim =         base['restricao_amendoim'].value_counts()
    frq_vegetarianismo =            base['vegetarianismo'].value_counts()
    frq_veganismo =                 base['veganismo'].value_counts()
    frq_semRestricao =              base['sem_restricao'].value_counts()
    frq_restricaoOutro =            base['restricao_outro'].value_counts()
    frq_identificacaoGenero =       base['identificacao_genero'].value_counts()
    frq_dataNascimento =            base['data_nascimento'].value_counts()
    frq_rendaMensal =               base['renda_mensal'].value_counts()
    frq_bairro =                    base['bairro'].value_counts()
    frq_cidade =                    base['cidade'].value_counts()
    frq_estado =                    base['estado'].value_counts()
    frq_outrosInteresses =          base['outros_interesses'].value_counts()
    frq_comoConheceu =              base['como_conheceu'].value_counts()
    frq_temCupomAmostra =           base['tem_cupom_amostra'].value_counts()
    frq_regiao =                    base['REGIAO'].value_counts()
    
    
    st.subheader("Distribuição: Você gosta de moda?")
    fig, ax = plt.subplots()
    frq_gostaModa.plot(kind='bar', ax=ax)
    ax.set_title('Frequência de resposta para "Você gosta de moda?"')
    ax.set_xlabel('Resposta')
    ax.set_ylabel('Frequência')
    st.pyplot(fig)
    
    
    st.subheader("Distribuição de tipos de pele")
    fig, ax = plt.subplots()
    ax.pie(frq_tipoPele, labels=frq_tipoPele.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal') 
    st.pyplot(fig)
    
    
    st.subheader("Proporcao de clientes por estado")
    fig, ax = plt.subplots()
    frq_regiao.plot(kind='bar', ax=ax)
    ax.set_title("Distribuicao de clientes por regiao")
    ax.set_xlabel('REGIAO')
    st.pyplot(fig)
    
    
if __name__ == '__main__':
    main()
