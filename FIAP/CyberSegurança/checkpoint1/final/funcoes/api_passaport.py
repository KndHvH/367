import requests as req
def api_passaport():
    lista_passaporte = []
    lista_arg = req.get("https://kndhvh.github.io/arg.json")
    arg = lista_arg.json()['arg']
    for i in arg:
        lista_passaporte.append(str(i['arg']))
    return lista_passaporte