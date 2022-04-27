import re

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
            #st.error
            print('[CUIDADO] Passaporte proibido, deter imediatamente!')
      else:
          #st.warning
        print('Passaporte Invalido!')