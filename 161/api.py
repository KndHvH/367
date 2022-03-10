'''
-pandas
-flask

'''
import pandas as pd
from flask import Flask


app = Flask(__name__)

#funcionalidades
def homepage():
    return 'Essa é a home page do site'


#rodar api
app.run()






'''tabela=pd.read_csv('list.csv')
total_vendas=tabela['Vendas'].sum()
print(total_vendas)'''