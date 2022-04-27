import re
from fuzzywuzzy import process

def getmatch_nome(input,lista):
    search_list = process.extract(input,lista)
    result=[]
    result2=[]

    for text in search_list:
        if text[1] > 90:
          result2.append(text)
        if text[1] > 50:
          result.append(text)

        if len(result2) > 0:
            return 2
        elif len(result) == 0:
            return 0
        return 1

def valid_nome(input_nome,lista_nome):
  if len(input_nome) > 4 and len(re.split('\s',input_nome)) >= 2:
      nome = getmatch_nome(input_nome,lista_nome)
      if nome == 2:
          #st.error
          print('[CUIDADO] Nome sujo, deter imediatamente!')
      elif nome == 1:
          # st.error
          print('[CUIDADO] Nome suspeito, favor investigar!')
      else:
          # st.sucess
          print('[VERIFICADO] Passageiro liberado para entrada no pais!')
  else:
      # st.warning
      print('Nome Invalido!')