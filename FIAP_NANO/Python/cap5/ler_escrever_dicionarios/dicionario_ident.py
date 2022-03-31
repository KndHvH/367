from ident import *

usuarios = {}

'importar(usuarios)'

opcao=pergunta()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        data_input(usuarios)

    elif opcao=="P":
        busca(usuarios)

    elif opcao=="E":
        remover(usuarios)

    else: #L
        listar(usuarios)


    opcao=pergunta()

salvar(usuarios)