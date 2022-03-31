
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
    idade = input("Digite a sua idade: ")

    x[login] = [nome,idade]

def busca(x):
    busca = input("Digite o login: ").lower()
    achou=0
    for i in x:
        if busca==i:
            achou=1
            print(
                "\nLogin:.....................:",i,
                "\nNome:......................:",x[i][0],
                "\nIdade:.....................:",x[i][1],
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
                "\nIdade:.....................:",x[i][1],
            )



def salvar(dicionario):
    with open ("bd.txt", "a") as arquivo:
        txt = []
        for i, j in dicionario.items():
            dic = [i,j]
            txt.append(dic)
        arquivo.write(str(txt))

def importar(dicionario):
    with open ("bd.txt", "r") as arquivo:
        txt = list(arquivo.read())
        for i in range(len(txt)):
            print(txt[0])
            dic = list(txt[i])
            i = dic[0]
            j = dic[1]
            dicionario = dict(i,j)




