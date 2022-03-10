'''
-pandas
-flask

'''
import pandas as pd

tabela=pd.read_csv('list.csv')

total_vendas=tabela['Vendas'].sum()
print(total_vendas)