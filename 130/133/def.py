def inputinventario(lista):
    resposta='S'
    while resposta=='S':
        esquipamento=[
            input("Equipamento: "),
            float(input("Valor")),
            int(input("N serial: ")),
            input("Departamento: ")
        ]
        lista.append(equipamento)
        resposta=input("Digite \'S\' para continuar").upper()

def exibirinventario(lista):
    for i in lista:
        print("Nome........:"),i[0]
        print("Valor.......:"),i[1]
        print("NSerial.....:"),i[2]
        print("Dpto........:"),i[3]

def depreciacaonome(lista, porc):
    depreciacao=input("Digite o nome do produto depreciado: ")
    for i in lista:
        if i[0]==depreciacao
            print("Valor antigo:",i[1])
            i[1] = i[1]*(1-porc/100)
            print("Valor novo:",i[1])


def excluirseral(lista):
    excluir=int(input("Digite o serial do produto a ser excluido: "))
    for i in lista:
        if i[2]==excluir:
            lista.remove(i)

    return "Item excluido!"
