def testtt(a):
    b='b'
    a.append(b)
    b='c'
    a.append(b)

def inputinventario(lista):
    resposta='S'
    while resposta=='S':
        equipamento=[
            input("Equipamento: ").upper(),
            float(input("Valor: ")),
            int(input("N serial: ")),
            input("Departamento: ").upper()
        ]
        lista.append(equipamento)
        resposta=input("Digite \'S\' para continuar cadastrando: ").upper()

def exibirinventario(lista):
    print("####################")
    for i in lista:
        print("Nome........:",i[0])
        print("Valor.......: %.2f"%i[1])
        print("NSerial.....:",i[2])
        print("Dpto........:",i[3])
        print("####################")


def localizarnome(lista):
  busca=input("Digite o nome do equipamento que deseja buscar: ").upper()
  for i in lista:
    if busca==i[0]:
      print("Valor..: %.2f"% i[1])
      print("Serial.:", i[2])

def depreciacaonome(lista, porc):
    depreciacao=input("Digite o nome do produto depreciado: ").upper()
    for i in lista:
        if i[0]==depreciacao:
            print("Valor antigo: %.2f"%i[1])
            i[1] = i[1]*(1-porc/100)
            print("Valor novo: %.2f"%i[1])


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
    if len(valores)>0:
        print("Equipamento mais caro %.2f"%max(valores))
        print("Equipamento mais barato %.2f"%min(valores))
        print("Ativo total %.2f"%sum(valores))
