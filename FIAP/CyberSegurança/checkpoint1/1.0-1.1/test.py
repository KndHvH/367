
import requests as req
import re
from fuzzywuzzy import process
from pyngrok import ngrok


def main():
    lista_nome = []
    lista_passaporte = []

    # Importando as apis em forma de lista
    def api(lista_nome, lista_passaporte):

        lista_interpol = req.get("https://cspinheiro.github.io/interpol.json")
        lista_arg = req.get("https://kndhvh.github.io/arg.json")

        # Limpando os dados
        arg = lista_arg.json()['arg']
        interpol = lista_interpol.json()['interpol']

        # colocando apenas o conteudo das duas APIs em 2 listas para facil leitura.
        for i in arg:
            lista_passaporte.append(i['arg'])

        for i in interpol:
            lista_nome.append(i['interpol'])

    api(lista_nome, lista_passaporte)

    # pedindo os dados pro usuario
    input_passaporte = input('Passaporte')
    input_nome = input('Nome Completo')

    # Limpando os dados inputados
    input_passaporte = re.sub('\D', '', input_passaporte)

    # funcao para validar os dados inputados e comparar com base de dados
    def valid(input_passaporte, input_nome, lista_nome, lista_passaporte):
        if 1==1:
            if len(input_passaporte) == 9 and len(input_nome) > 4 and len(re.split('\s', input_nome)) >= 2:
                passa = getmatch(lista_passaporte, input_passaporte)
                if passa == 2:
                    print('[CUIDADO] Passaporte proibido, deter imediatamente!')
                elif passa == 1:
                    print('[CUIDADO] Passaporte suspeito, favor investigar!')
                else:
                    nome = getmatch(lista_nome, input_nome)

                if nome == 2:
                    print('[CUIDADO] Nome sujo, deter imediatamente!')
                elif nome == 1:
                    print('[CUIDADO] Nome suspeito, favor investigar!')
                else:
                    print('[VERIFICADO] Passageiro liberado para entrada no pais!')
            else:
                print('Nome ou passaporte Invalidos!')

    def getmatch(field, lista_pn):

        search_list = process.extract(field, lista_pn)
        result = []
        result2 = []

        for text in search_list:
            if text[1] > 90:
                result2.append(text)
            if text[1] > 50:
                result.append(text)

            if len(result2) > 0:
                return 2
            elif len(result) == 0:
                return 0
            return 1

    valid(input_passaporte, input_nome, lista_nome, lista_passaporte)


if __name__ == '__main__':
    main()