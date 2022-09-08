
import random

print("MENU - OusadIA")

# Função
# A função do nosso programa seria poder converter os comentarios de um serviço ou produto determinado,
# Em dados quantitativos
# para poder analizar de uma forma simples, a mensagem e opinião dos clientes.

decisao = 1
comentario = []
notas = []
contador = 0
entrada = ''
total = 0
newData = 0
sizeNotas = 0

while decisao != 0:
    print("-----------------------")
    print("1 - Inserir comentarios do clientes")
    print("2 - Exibir todos os comentarios")
    print("3 - Converter dados quali. para quant.")
    print("4 - Exibir pontuações")
    print("5 - Media pontuaçao total")
    print("0 - SAIR")
    try:

        decisao = int(input("mDigite a opção desejada: "))

        if decisao == 1:
            entrada = ''

            while entrada!='0':
                entrada = input(f"Digite o comentario do cliente numero {contador+1}, Digite 0 para sair!\n")
                if entrada!='0':
                    comentario.append(entrada)
                    contador += 1
                    newData = 1

        if decisao == 2:
            if comentario==[]:
                print("Lista de comentarios vazia!")
            else:

                for i in range(0,contador):
                    print(f"Comentario cliente numero {i+1}: {comentario[i]}")

        if decisao == 3:
            # nesse campo, o programa iria atribuir uma nota de 0 a 5 baseado no comentario do cliente,
            # Como ainda nao desenvolvemos um recurso capaz de realizar essa tarefa, irenos escolher os
            # numeros aleatoriamente.
            if newData == 0:
                print("Novos dados nao foram inseridos!")
            else:
                for i in range(0,contador-sizeNotas):
                    numero = random.randrange(0,6)
                    notas.append(numero)
                newData=0
                sizeNotas = contador

        if decisao == 4:
            if notas==[] or sizeNotas != contador:
                print("Favor converter dados!")
            else:
                for i in range(0,contador):
                    print(f"Nota cliente numero {i+1}: {notas[i]}")

        if decisao == 5:
            if contador == 0:
                print("Favor inserir os comentarios!")
            elif notas==[] or sizeNotas != contador:
                print("Favor converter dados!!")
            else:
                total = 0
                for i in range(0,contador):
                     total += notas[i]
                media = total / contador
                print(f"Media: {media:.2f}")


    except ValueError:
        print('Favor inserir numero valido!')










