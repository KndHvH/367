

equip=[]
val=[]
ser=[]
dpto=[]
resp='S'

while resp=='S':
    equip.append(input("Equipamentos: ").upper())
    val.append(input("Valor: ").upper())
    ser.append(input("Serial: ").upper())
    dpto.append(input("Departamento: ").upper())
    resp = input("Digite \"S\" para continuar: ").upper()

busca=input("Digite o nome do equipamento que deseja buscar: ").upper()
for i in range(0,len(equip)):
  if busca==equip[i]:
    print("Produto......: ", equip[i])
    print("Valor........:  R$", val[i])
    print("Serial.......: ", ser[i])
    print("Departamento.: ", dpto[i])