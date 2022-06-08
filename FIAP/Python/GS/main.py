
# RM 94199 - Matias Cornelsen Herklotz
# RM 93821 - Gustavo Jordão Santos
# RM 94026 - Daniel Faria de Barros

print("\033[91m\033[1mVOTAÇÃO - SEGUNDO TURNO\033[0m")

legenda = ['Nulo','Blue','Red']
decisao = 1
listaVotos = []
tamanhoLista = 0
totalVotos = 0


while decisao != 0:
    print("\033[1m-----------------------\033[0m")
    print("\033[92m1\033[0m – Efetuar a votação")
    print("\033[92m2\033[0m – Exibir o Relatório dos Votos")
    print("\033[92m3\033[0m – Efetuar a apuração | Exibir o resultado")
    print("\033[92m4\033[0m – Mostrar o percentual dos votos")
    print("\033[92m0\033[0m – SAIR")
    try:

        decisao = int(input("\033[92mDigite a opção desejada:\033[0m "))

        if decisao == 1:
            voto = 1
            while voto != 0:
                print("\033[1m-----------------------\033[0m")
                print("\033[92m1\033[0m – Votar Candidato Blue")
                print("\033[92m2\033[0m – Votar Candidato Red")
                print("\033[92m3\033[0m – Voto Nulo")
                print("\033[92m0\033[0m – SAIR")
                voto = int(input("\033[92mDigite a opção desejada:\033[0m "))
                if voto!=0:
                    listaVotos.append(voto)
                    tamanhoLista += 1
            for i in range(0, tamanhoLista):
                if listaVotos[i] != 1 and listaVotos[i] != 2:
                    listaVotos[i] = 0

        if decisao == 2:
            if listaVotos != []:
                for i in range(0,tamanhoLista):
                    print(f'Voto da pessoa {i+1} foi {legenda[listaVotos[i]]}')
            else:
                print('\033[91m\033[1mNenhum Voto Computado!\033[0m ')

        if decisao == 3:
            votosNulo = 0
            votosBlue = 0
            votosRed = 0
            totalVotos = 0
            for i in range(0, tamanhoLista):
                    if listaVotos[i] == 0:
                        votosNulo += 1
                    elif listaVotos[i] == 1:
                        votosBlue += 1
                    else:
                        votosRed += 1
            totalVotos = votosRed+votosBlue+votosNulo
            print("\033[1m-----------------------\033[0m")
            print(f'\033[93mTotal de votos Nulos: {votosNulo}\033[0m')
            print(f'\033[94mTotal de votos Blue: {votosBlue}\033[0m')
            print(f'\033[91mTotal de votos Red: {votosRed}\033[0m')
            print(f'\033[92mTotal de votos: {totalVotos}\033[0m')

        if decisao == 4:
            if listaVotos == []:
                print('\033[91m\033[1mNenhum Voto Computado!\033[0m')
            elif totalVotos == 0:
                print('\033[91m\033[1mResultado não apurado!\033[0m')
            else:
                print("\033[1m-----------------------\033[0m")
                print(f'\033[93mTotal de votos Nulos: {votosNulo}\nPorcentagem: {(votosNulo/totalVotos)*100:.2f}%\033[0m')
                print(f'\033[94mTotal de votos Blue: {votosBlue}\nPorcentagem: {(votosBlue/totalVotos)*100:.2f}%\033[0m')
                print(f'\033[91mTotal de votos Red: {votosRed}\nPorcentagem: {(votosRed/totalVotos)*100:.2f}%\033[0m')
                print(f'\033[92mTotal de votos: {totalVotos}\nPorcentagem: {(totalVotos/totalVotos)*100:.2f}%\033[0m')

    except ValueError:
        print('\033[91m\033[1mFavor inserir numero valido!\033[0m')










