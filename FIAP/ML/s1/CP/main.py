
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from pycaret.classification import *

st.set_page_config( page_title = 'Simulador - Case Ifood - Grupo OusadIa',
                    page_icon = './images/logo_fiap.png',
                    layout='centered',
                    initial_sidebar_state = 'expanded')

st.title('Simulador - Conversão de Vendas')

with st.sidebar:
    c1, c2 = st.columns(2)
    c1.image('./images/logo_fiap.png', width = 100)
    c2.write('')
    c2.subheader('Auto ML - Fiap [v1.1-OuIa]')

    database = st.radio('Fonte dos dados de entrada (X):', ('CSV', 'Online'))

    if database == 'CSV':
        st.info('Upload do CSV')
        file = st.file_uploader('Selecione o arquivo CSV', type='csv')

#Tela principal
if database == 'CSV':
    if file:
        #carregamento do CSV
        Xtest = pd.read_csv(file)

        #carregamento / instanciamento do modelo pkl
        mdl_lgbm = load_model('./pickle_lgbm_pycaret')

        #predict do modelo
        ypred = predict_model(mdl_lgbm, data = Xtest, raw_score = True)

        with st.expander('Visualizar CSV carregado:', expanded = False):
            c1, _ = st.columns([2,4])
            qtd_linhas = c1.slider('Visualizar quantas linhas do CSV:', 
                                    min_value = 5, 
                                    max_value = Xtest.shape[0], 
                                    step = 10,
                                    value = 5)
            st.dataframe(Xtest.head(qtd_linhas))

        with st.expander('Visualizar Predições:', expanded = True):
            c1, _, c2, c3 = st.columns([2,.5,1,1])
            treshold = c1.slider('Treshold (ponto de corte para considerar predição como True)',
                                min_value = 0.0,
                                max_value = 1.0,
                                step = .1,
                                value = .5)
            qtd_true = ypred.loc[ypred['Score_True'] > treshold].shape[0]

            c2.metric('Qtd clientes True', value = qtd_true)
            c3.metric('Qtd clientes False', value = len(ypred) - qtd_true)
            
            def color_pred(val):
                color = 'olive' if val > treshold else 'orangered'
                return f'background-color: {color}'

            tipo_view = st.radio('', ('Completo', 'Apenas predições'))
            if tipo_view == 'Completo':
                df_view = ypred.copy()
            else:
                df_view = pd.DataFrame(ypred.iloc[:,-1].copy())

            st.dataframe(df_view.style.applymap(color_pred, subset = ['Score_True']))

            csv = df_view.to_csv(sep = ';', decimal = ',', index = True)
            st.markdown(f'Shape do CSV a ser baixado: {df_view.shape}')
            st.download_button(label = 'Download CSV',
                            data = csv,
                            file_name = 'Predicoes.csv',
                            mime = 'text/csv')

        
    else:
        st.warning('Arquivo CSV não foi carregado')

if database == 'Online':
    with st.form("Single Consult"):
        
        st.header("Consulta Unica")
        
        form_age = st.number_input("Age",step=1)
        form_n_kids = st.number_input("Number Of Kids",step=1)
        form_n_teens = st.number_input("Number Of Teens",step=1)
        form_income = st.number_input("Income",step=0.01)

        

        form_education = st.selectbox(
            'Education Level',
            options=['Basic','2n Cycle','Graduation','Master','Doctor']
        )
        form_marital = st.selectbox(
            'Marital Status',
            options=['Single','Married','Together','Divorced','Alone','Widow','Absurd']
        )        
        form_cmps = st.multiselect(
                    'Accepted Cmps',
                    ['Cmp1', 'Cmp2', 'Cmp3', 'Cmp4','Cmp5'])
        
        form_complain = st.checkbox("Complain")
        

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(form_cmps)




