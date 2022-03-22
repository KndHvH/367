inv=[]
resp = "S"

while resp == "S":
  equip=[input("Equipamento: "),
        float(input("Valor: ")),
        int(input("Número Serial: ")),
        input("Departamento: ")]

  inv.append(equip)
  resp = input("Digite \"S\" para continuar: ").upper()

for i in inv:
  print("Nome.........: ", i[0])
  print("Valor........: ", i[1])
  print("Serial.......: ", i[2])
  print("Departamento.: ", i[3])

busca=input("Digite o nome do equipamento que deseja buscar: ")
for i in inv:
  if busca==i[0]:
    print("Valor..: ", i[1])
    print("Serial.:", i[2])

depr=input("Digite o nome do equipamento que será depreciado: ")
for i in inventario:
  if depre==i[0]:
    print("Valor antigo: ", i[1])
    i[1] = i[1] * 0.9
    print("Novo valor: ", i[1])

serial=int(input("Digite o serial do equipamento que será excluído: "))
for i in inv:
  if i[2]==serial:
    #inv.remove(i)
    del inv[i]  

for elemento in inventario:
  print("Nome.........: ", i[0])
  print("Valor........: ", i[1])
  print("Serial.......: ", i[2])
  print("Departamento.: ", i[3])