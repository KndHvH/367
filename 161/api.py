'''
-pandas
-flask

'''
import gcloud
import pandas as pd
from flask import Flask

gcloud.init

app = Flask(__name__)

#funcionalidades
@app.route('/')
def homepage():
    return 'Essa é a home page do site'

@app.route('/contatos')
def contatos():
    return 'Essa é a page de contatos do site'


#rodar api
#app.run()
gcloud.app.deploy







'''tabela=pd.read_csv('list.csv')
total_vendas=tabela['Vendas'].sum()
print(total_vendas)'''