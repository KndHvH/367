import pandas as pd
from flask import Flask, jsonify


app = Flask(__name__)



#funcionalidades
@app.route('/')
def main():
    dados = []
    link = 'http://127.0.0.1:5000/lista'
    conta=[]
    conta=[
        input("Digite seu nome:"),
        input("Digite seu email"),
    ]
    dados.append(conta)

    print("Dados:")
    print(link)

    return (
        input("Digite seu nome:"),

    )





@app.route('/lista')
def lista():
    return ''

@app.route('/tabela')
def tabela():

    tabela=pd.read_csv('list.csv')

    total_vendas=tabela['Vendas'].sum()

    resposta={'total_vendas': total_vendas}

    return jsonify(resposta)


#rodar api
app.run()








'''tabela=pd.read_csv('list.csv')
total_vendas=tabela['Vendas'].sum()
print(total_vendas)'''