
def pergunta():
    return input("_______________________________\n" +
          "o que deseja realizar?\n" +
          "<I> - Para Inserir um usuario\n" +
          "<P> - Para Pesquisar um usuario\n" +
          "<E> - Para Excluir um usuario\n" +
          "<L> - Para Listar todos os usuarios\n" +
          "<S> - Para Sair do programa: ").upper()

def data_input(x):
    login = input("Digite o login: ").lower()
    nome = input("Digite o seu nome: ")
    data = input("Digite a ultima data de acesso: ")
    estacao = input("Digite a ultima estação acessada: ").lower()

    x[login] = [nome,data,estacao]
    salvar(x)
def busca(x):
    busca = input("Digite o login: ").lower()
    achou=0
    for i in x:
        if busca==i:
            achou=1
            print(
                "\nLogin:.....................:",i,
                "\nNome:......................:",x[i][0],
                "\nUltima data de acesso:.....:",x[i][1],
                "\nUltma estacao acessada:....:",x[i][2],
            )
    if achou!=1:
        print("Usuario não encontrado!")

def remover(x):
    alvo = input("Digite o login do usuario que deseja remover: ").lower()
    achou=0
    for i in x:
        if alvo == i:
            print(f"SOB CONSTRUCAO")
            print(f"Login {i} deletado!")
            del i
            achou=1
    if achou != 1:
        print("Usuario não encontrado!")

def listar(x):
        print("..........Lista...........:",)
        for i in x:
            print(
                "\nLogin:.....................:",i,
                "\nNome:......................:",x[i][0],
                "\nUltima data de acesso:.....:",x[i][1],
                "\nUltma estacao acessada:....:",x[i][2],
            )



def salvar(dicionario):
    import pickle

    with open("bd.pkl", "ab") as tf:
        pickle.dump(dicionario, tf)




'''    with open ("bd.txt","a") as arquivo:
        for chave,valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor) + "\n")'''

'''def importar(dicionario):
    with open("bd.txt", "r") as arquivo:
        for i in arquivo.readlines():
            string = i
            l = string.split(':')
            login = l[0]

            j = l[1]
            j = j.replace("[", "")
            j = j.replace("]", "")
            j = j.replace(" ", "")
            j = j.replace("'", "")

            items = j.split(',')

            dicionario[login] = [items[0],items[1],items[2]]'''


