#dicionario
usuarios = {}

#lista
emails = ["abc@gmail.com","def@gmail.com"]

#tupla = lista de (0,1,2... + lista de emails)
tupla = list(enumerate(emails))
#[(0, 'abc@gmail.com'), (1, 'def@gmail.com')]

# for i dentro do tamanho de tupla, no caso 2
for i in range(0, len(tupla)):

    #print tupla [0/1] posição [1]
    print("Email: ", tupla[i][1])

    #dicionario [tupla[i]] -> dicionario[0/1] = [input,input2]
    usuarios[tupla[i]] = [input("Digite o nome: "),input("Digite o nivel: ")]
    #{(0, 'abc@gmail.com'): ['abece', '33'], (1, 'def@gmail.com'): ['deefee', '44']}

print(usuarios)
for i, dado in usuarios.items():
    print("Usuario.:",i[0])
    print("Email...:",i[1])
    print("Nome....:",dado[0])
    print("Nivel...:",dado[1])