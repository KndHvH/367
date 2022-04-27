def valid_passa(input_passaporte,lista_passaporte):
      if len(input_passaporte) == 9:
        passa = getmatch(lista_passaporte,input_passaporte)
        if passa == 2:
          st.error('[CUIDADO] Passaporte proibido, deter imediatamente!')
        elif passa == 1:
          st.error('[CUIDADO] Passaporte suspeito, favor investigar!')
      else:
        st.warning('Passaporte Invalido!')