
print("VOTAÇÃO - SEGUNDO TURNO")

decisao = 1
voto = 1
listaVotos = []

while decisao != 0:
    print("-----------------------")
    print("1 – Efetuar a votação")
    print("2 – Exibir o Relatório dos Votos")
    print("3 – Efetuar a apuração | Exibir o resultado")
    print("4 – Mostrar o percentual dos votos")

    decisao = int(input("Digite a opção desejada:_"))

    if decisao == 1:
        while voto != 0:
            print("-----------------------")
            print("1 – Votar Candidato: Blue")
            print("2 – Votar Candidato: Red")
            print("0 – SAIR")
            voto = int(input("Digite a opção do candidato desejado:_"))











