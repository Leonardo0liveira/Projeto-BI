import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def prepare(base):
    novas_colunas = {
        '#': 'id',
        'Você gosta de moda?': 'gosta_moda',
        'Você se considera uma pessoa artística?': 'pessoa_artistica',
        'Você usa maquiagem?': 'usa_maquiagem',
        'Tônico': 'uso_tonico',
        'Cleanser': 'uso_cleanser',
        'Cleansing Oil': 'uso_cleansing_oil',
        'Creme para os olhos': 'uso_creme_olhos',
        'Maquiagem para os olhos': 'maquiagem_olhos',
        'Maquiagem para os lábios': 'maquiagem_labios',
        'Maquiagem para o rosto': 'maquiagem_rosto',
        'Esmalte': 'uso_esmalte',
        'Máscara facial': 'uso_mascara_facial',
        'Máscara capilar': 'uso_mascara_capilar',
        'Protetor solar': 'uso_protetor_solar',
        'Produto para modelar cabelo': 'uso_produto_modelar_cabelo',
        'Fragrância / perfume': 'uso_perfume',
        'Esfoliante facial': 'uso_esfoliante_facial',
        'Tratamento para manchas/ Tratamento para acne': 'tratamento_manchas_acne',
        'Sérum/ óleo de tratamento': 'uso_serum_oleo',
        'Removedor de maquiagem/ Água micelar': 'uso_removedor_maquiagem',
        'Tópicos medicados (por exemplo, Tretinoína)': 'uso_topicos_medicados',
        'Não tenho uma rotina de beleza': 'sem_rotina_beleza',
        'Onde você costuma comprar seus produtos de beleza?': 'onde_compra_produtos_beleza',
        'Qual é seu tipo de pele?': 'tipo_pele',
        'O que você procura ao comprar um produto?': 'criterio_compra_produto',
        'Você (ou alguém na sua família) gosta de brinquedos ou jogos?': 'gosta_brinquedos_jogos',
        'Você pratica esportes?': 'pratica_esportes',
        'Você tem um pet?': 'tem_pet',
        'Você gosta de decorar a sua casa?': 'gosta_decoracao',
        'Você consome alimentos saudáveis com frequência?': 'consome_alimentos_saudaveis',
        'Você é fã de gastronomia?': 'fan_gastronomia',
        'Você gosta de mexer com carros?': 'gosta_carros',
        'Você se tornou mãe ou pai recentemente?': 'recentemente_pai_mae',
        'Você gosta de bebidas alcoólicas?': 'gosta_bebidas_alcoolicas',
        'Você se interessa por cuidados pessoais?': 'interesse_cuidados_pessoais',
        'Você é fanático pelas últimas tecnologias?': 'fan_tecnologia',
        'Você é criador de conteúdo ou influencer?': 'criador_influencer',
        'Moda': 'interesse_moda',
        'Arte': 'interesse_arte',
        'Maquiagem': 'interesse_maquiagem',
        'Brinquedos ou jogos': 'interesse_brinquedos_jogos',
        'Esportes': 'interesse_esportes',
        'Pets': 'interesse_pets',
        'Decoração': 'interesse_decoracao',
        'Bem-estar': 'interesse_bem_estar',
        'Gastronomia': 'interesse_gastronomia',
        'Carros': 'interesse_carros',
        'Parentalidade': 'interesse_parentalidade',
        'Bebidas': 'interesse_bebidas',
        'Cuidados pessoais': 'cuidados_pessoais',
        'Tecnologia': 'interesse_tecnologia',
        'Lactose': 'restricao_lactose',
        'Glúten': 'restricao_gluten',
        'Soja': 'restricao_soja',
        'Ovo': 'restricao_ovo',
        'Amendoim': 'restricao_amendoim',
        'Vegetarianismo': 'vegetarianismo',
        'Veganismo': 'veganismo',
        'Não tenho restrição': 'sem_restricao',
        'Outro': 'restricao_outro',
        'First name': 'nome',
        'Last name': 'sobrenome',
        'Como você se identifica?': 'identificacao_genero',
        'Qual é a sua data de nascimento?': 'data_nascimento',
        'Qual é a faixa de renda mensal da sua família?': 'renda_mensal',
        'Qual é o seu email pessoal?': 'email',
        'Bairro': 'bairro',
        'Cidade': 'cidade',
        'Estado': 'estado',
        'O que mais te interessa?': 'outros_interesses',
        'Como você conheceu a Experimentaí?': 'como_conheceu',
        'Tem um cupom de amostra?': 'tem_cupom_amostra',
        'Ao _prosseguir_ você afirma que leu e está de acordo com o Aviso de Privacidade e Termos de Uso da Experimentaí.': 'concorda_termos',
        'utm_source': 'utm_source',
        'Response Type': 'tipo_resposta',
        'Start Date (UTC)': 'data_inicio',
        'Stage Date (UTC)': 'data_estagio',
        'Submit Date (UTC)': 'data_envio',
        'Network ID': 'id_rede',
        'Tags': 'tags'
    }

    base.rename(columns=novas_colunas, inplace=True)    
    
    
    

    # Carregar o arquivo de regiões 'UF_regioes.csv'
    regioes = pd.read_csv('prep/UF_regioes.csv', sep=',')

    # Padronizar os valores da coluna 'Estado' em 'base' e 'ESTADO' em 'regioes'
    base['estado'] = base['estado'].str.strip().str.upper()
    regioes['ESTADO'] = regioes['ESTADO'].str.strip().str.upper()
    # Realizar o merge com base nas colunas 'Estado' e 'ESTADO'
    base = pd.merge(base, regioes, left_on='estado', right_on='ESTADO', how='left')
    

    del base['tags']
    del base['data_estagio']
    del base['id_rede']
    del base['utm_source']
    del base['data_envio']
    del base['data_inicio']
    del base['concorda_termos']
    del base['tipo_resposta']
    del base['email']
    del base['nome']
    del base['sobrenome']
    del base['ESTADO']
    del base['id']
    del base['UF']
 

    
    # Novas colunas binárias para substituição de 1 por "Sim" e 0 por "Não"
    binary_columns = [
     'gosta_moda', 'pessoa_artistica', 'usa_maquiagem', 'uso_tonico',
     'uso_cleanser', 'uso_cleansing_oil', 'uso_creme_olhos',
     'maquiagem_olhos', 'maquiagem_labios', 'maquiagem_rosto', 'uso_esmalte',
     'uso_mascara_facial', 'uso_mascara_capilar', 'uso_protetor_solar',
     'uso_produto_modelar_cabelo', 'uso_perfume', 'uso_esfoliante_facial',
     'tratamento_manchas_acne', 'uso_serum_oleo', 'uso_removedor_maquiagem',
     'uso_topicos_medicados', 'sem_rotina_beleza', 'gosta_brinquedos_jogos', 
     'pratica_esportes', 'tem_pet', 'gosta_decoracao', 'consome_alimentos_saudaveis', 
     'fan_gastronomia', 'gosta_carros', 'recentemente_pai_mae', 'gosta_bebidas_alcoolicas',
     'interesse_cuidados_pessoais', 'fan_tecnologia', 'criador_influencer', 
     'interesse_moda', 'interesse_arte', 'interesse_maquiagem', 'interesse_brinquedos_jogos',
     'interesse_esportes', 'interesse_pets', 'interesse_decoracao', 'interesse_bem_estar',
     'interesse_gastronomia', 'interesse_carros', 'interesse_parentalidade', 'interesse_bebidas',
     'cuidados_pessoais', 'interesse_tecnologia'
     ]
    
    # Substituir 1 por 'Sim' e 0 por 'Não' nas colunas binárias
    base.loc[:, binary_columns] = base[binary_columns].replace({1: 'Sim', 0: 'Não'})    
    
    base.to_csv('BaseTratada.csv', index =False)
    
    return base
    
    
   