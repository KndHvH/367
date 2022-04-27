def valid_nome(input_nome,lista_nome):
  if len(input_nome) > 4 and len(re.split('\s',input_nome)) >= 2:
      nome = getmatch(lista_nome,input_nome)
      if nome == 2:
        st.error('[CUIDADO] Nome sujo, deter imediatamente!')
      elif nome == 1:
        st.error('[CUIDADO] Nome suspeito, favor investigar!')
      else:
        st.sucess('[VERIFICADO] Passageiro liberado para entrada no pais!')
  else:
      st.warning('Nome Invalido!')