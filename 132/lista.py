

equip=[]
val=[]
ser=[]
dpto=[]
resp='S'

while resp=='S':
    equip.append(input("Equipamentos: "))
    val.append(input("Valor: "))
    ser.append(input("Serial: "))
    dpto.append(input("Departamento: "))
    resp = input("Digite \"S\" para continuar: ").upper()

for i in range(0,len(equip)):
    print("Equipamento..: ", (i + 1))
    print("Nome.........: ", equip[i])
    print("Valor........: ", val[i])
    print("Serial.......: ", ser[i])
    print("Departamento.: ", dpto[i])
    print(".............:")
