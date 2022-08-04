import streamlit as st
import json
import requests as req
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from pyngrok import ngrok

def main():
    html_temp = """ <div style ="background-color:blue;padding:13px">
                      <h1 style = "color:white;text-align:center;">Ola parceiro, publique seus itens</h1>
                    </dic>
                """
    st.markdown(html_temp, unsafe_allow_html = True)
    item = st.text_input("item")

    def verificarNome(item):
      res = req.get("https://www.github.com/kndhvh/kndhvh.github.io")
      dict = res.json()['eleicao']
      lista_fuzy = process.extract(item,dict)
      resultado = []
      for sublinha in lista_fuzy:
        if sublinha[1]> 80:
          resultado.append(sublinha)
      if len(resultado) >= 1:
        st.success("Atencao as fake news")

    if st.button("Verificar"):
      verificarNome(item)
if __name__=='__main__':
  main()
