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

def localizarnome(lista):
  busca=input("Digite o nome do equipamento que deseja buscar: ")
  for i in lista:
    if busca==i[0]:
      print("Valor..: ", i[1])
      print("Serial.:", i[2])

def depreciacaonome(lista, porc):
    depreciacao=input("Digite o nome do produto depreciado: ")
    for i in lista:
        if i[0]==depreciacao:
            print("Valor antigo:",i[1])
            i[1] = i[1]*(1-porc/100)
            print("Valor novo:",i[1])


def excluirserial(lista):
    excluir=int(input("Digite o serial do produto a ser excluido: "))
    for i in lista:
        if i[2]==excluir:
            lista.remove(i)

    return "Item excluido!"

def resumovalores(lista):
    valores=[]
    for i in lista:
        valores.append(i[1])
    if len(valores>0):
        print("Equipamento mais caro",max(valores))
        print("Equipamento mais barato",min(valores))
        print("Total de equipamentos",sum(valores))
