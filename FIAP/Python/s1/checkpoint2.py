
import random

print("\033[91m\033[1mMENU - OusadIA\033[0m")

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
    print("\033[1m-----------------------\033[0m")
    print("\033[92m1\033[0m – Inserir comentarios do clientes")
    print("\033[92m2\033[0m – Exibir todos os comentarios")
    print("\033[92m3\033[0m – Converter dados quali. para quant.")
    print("\033[92m4\033[0m – Exibir pontuações")
    print("\033[92m5\033[0m – Media pontuaçao total")
    print("\033[92m0\033[0m – SAIR")
    try:

        decisao = int(input("\033[92mDigite a opção desejada:\033[0m "))

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
                print("\033[91m\033[1mLista de comentarios vazia!\033[0m")
            else:

                for i in range(0,contador):
                    print(f"Comentario cliente numero {i+1}: {comentario[i]}")

        if decisao == 3:
            # nesse campo, o programa iria atribuir uma nota de 0 a 5 baseado no comentario do cliente,
            # Como ainda nao desenvolvemos um recurso capaz de realizar essa tarefa, irenos escolher os
            # numeros aleatoriamente.
            if newData == 0:
                print("\033[91m\033[1mNovos dados nao foram inseridos!\033[0m")
            else:
                for i in range(0,contador-sizeNotas):
                    numero = random.randrange(0,6)
                    notas.append(numero)
                newData=0
                sizeNotas = contador

        if decisao == 4:
            if notas==[] or sizeNotas != contador:
                print("\033[91m\033[1mFavor converter dados!\033[0m")
            else:
                for i in range(0,contador):
                    print(f"Nota cliente numero {i+1}: {notas[i]}")

        if decisao == 5:
            if contador == 0:
                print("\033[91m\033[1mFavor inserir os comentarios!\033[0m")
            elif notas==[] or sizeNotas != contador:
                print("\033[91m\033[1mFavor converter dados!!\033[0m")
            else:
                total = 0
                for i in range(0,contador):
                     total += notas[i]
                media = total / contador
                print(f"\033[94m\033[1mMedia: {media:.2f}\033[0m")


    except ValueError:
        print('\033[91m\033[1mFavor inserir numero valido!\033[0m')










