from ident import *
usuarios = {}

opcao=pergunta()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        data_input(usuarios)
    elif opcao=="P":
        busca(usuarios)
    opcao=pergunta()