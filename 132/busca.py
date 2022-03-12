

equip=[]
val=[]
ser=[]
dpto=[]

novos=input("Digite \'S\' para cadastrar novos produtos: ").upper()

while novos=='S':
    equip.append(input("Equipamentos: ").upper())
    val.append(float(input("Valor: ")))
    ser.append(input("Serial: ").upper())
    dpto.append(input("Departamento: ").upper())
    novos = input("Digite \"S\" para continuar: ").upper()


busca_verif='N'

while busca_verif=='N':
    busca = input("Digite o nome do equipamento que deseja buscar: ").upper()
    for i in range(0,len(equip)):
      if busca==equip[i]:
        print("Produto......: ", equip[i])
        print("Valor........:  R$", val[i])
        print("Serial.......: ", ser[i])
        print("Departamento.: ", dpto[i])
        selecionado=[equip[i],val[i],ser[i],dpto[i]]

    busca_verif=input("Digite \'S\' se esse é o produto que procura: ").upper()


depreciacao=input("Digite \'S\' para editar o valor do produto selecionado: ").upper()

while depreciacao=='S':
4567899000000