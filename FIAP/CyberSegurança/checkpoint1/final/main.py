import streamlit as st
import requests as req
import re
from fuzzywuzzy import process
from pyngrok import ngrok

from funcoes.api_passaport import *
from funcoes.api_nome import *
from funcoes.validar_passaporte import *
from funcoes.validar_nome import *
from funcoes.getmatch_nome import *
from funcoes.getmatch_passa import *

def main():

    lista_passaporte = api_passaport()
    lista_nome = api_nome()


    # print(lista_passaporte)
    # print(lista_nome)

    #st fix
    input_passaporte = input('Passaporte')
    input_nome = input('Nome Completo')

    input_passaporte = re.sub('\D', '', input_passaporte)

    if st.button("Verificar"):
        valid_passa()
        valid_nome()




if __name__ == '__main__':
    main()