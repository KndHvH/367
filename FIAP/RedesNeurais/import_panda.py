import pandas as pd

dados = pd.read_excel("lista_facul.xlsx", index_col="ID")

print(dados)
escolas = dados.T

print(escolas)