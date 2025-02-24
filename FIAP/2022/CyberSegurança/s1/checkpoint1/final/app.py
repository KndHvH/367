
import streamlit as st
import requests as req
import re
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from pyngrok import ngrok

def main():
    html_temp = """ <div style ="background-color:blue;padding:13px">
                      <h1 style = "color:white;text-align:center;">Verificador Imigração - PFA</h1>
                    </dic>
                """

    st.markdown(html_temp, unsafe_allow_html = True)
    lista_passaporte = api_passaport()
    lista_nome = api_nome()

    lista_passaporte= regexlist(lista_passaporte)

    input_passaporte = st.text_input('Passaporte')
    input_nome = st.text_input('Nome Completo')

    input_passaporte = re.sub('\D', '', input_passaporte)

    if st.button("Verificar"):
      clear = 0
      clear = valid_passa(input_passaporte,lista_passaporte)
      if clear == 1:
        valid_nome(input_nome,lista_nome)

def api_nome():
    lista_nome = []
    lista_interpol = req.get("https://cspinheiro.github.io/interpol.json")
    interpol = lista_interpol.json()['interpol']
    for i in interpol:
        lista_nome.append(i['interpol'])

    return lista_nome

def api_passaport():
    lista_passaporte = []
    lista_arg = req.get("https://kndhvh.github.io/arg.json")
    arg = lista_arg.json()['arg']
    for i in arg:
        lista_passaporte.append(str(i['arg']))
    return lista_passaporte

def regexlist(lista):

    a='(?i)'

    for i in lista:
        a += f"({i})|"

    a = a[:-1]

    return a

def getmatch_nome(input,lista):
    search = process.extractOne(input,lista,scorer=fuzz.token_sort_ratio)
    if search[1] > 80:
      return 1
    return 0
        

def valid_nome(input_nome,lista_nome):
  if len(input_nome) > 4 and len(re.split('\s',input_nome)) >= 2:
      nome = getmatch_nome(input_nome,lista_nome)
      if nome == 1:
        st.error('[CUIDADO] Nome suspeito, favor investigar!')
      if nome == 0:
        st.success('[VERIFICADO] Passageiro liberado para entrada no pais!')
  else:
      st.warning('Nome Invalido!')

def getmatch_passa(input,lista):
    match = re.search(lista,input)

    if match:
        return 1
    else:
        return 0

def valid_passa(input_passaporte,lista_passaporte):
      if len(input_passaporte) == 9:
        passa = getmatch_passa(input_passaporte,lista_passaporte)
        if passa == 1:
            st.error('[CUIDADO] Passaporte proibido, deter imediatamente!')
            return 0
        else:
          return 1
      else:
        st.warning('Passaporte Invalido!')

if __name__ == '__main__':
    main()
