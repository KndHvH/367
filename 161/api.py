import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

#funcionalidades
@app.route('/')
def main():
    return 'home'

@app.route('/lista')
def lista():
    return ''

@app.route('/tabela')
def tabela():

    tabela=pd.read_csv('list.csv')

    total_vendas=tabela['Vendas'].sum()

    resposta={'total_vendas': total_vendas}

    return resposta


#rodar api
app.run()








'''tabela=pd.read_csv('list.csv')
total_vendas=tabela['Vendas'].sum()
print(total_vendas)'''