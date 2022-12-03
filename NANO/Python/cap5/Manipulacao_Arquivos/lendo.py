with open("arquivo1.txt","r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)