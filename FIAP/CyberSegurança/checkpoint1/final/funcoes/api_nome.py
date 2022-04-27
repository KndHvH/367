import requests as req
def api_nome():
    lista_nome = []
    lista_interpol = req.get("https://cspinheiro.github.io/interpol.json")
    interpol = lista_interpol.json()['interpol']
    for i in interpol:
        lista_nome.append(i['interpol'])

    return lista_nome