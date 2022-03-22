
def pergunta():
    return input("o que deseja realizar?\n" +
          "<I> - Para Inserir um usuario\n" +
          "<P> - Para Pesquisar um usuario\n" +
          "<E> - Para Excluir um usuario\n" +
          "<L> - Para Listar um usuario\n" +
          "<S> - Para Sair do programa: ").upper()

def data_input(x):
    login = input("Digite o login: ").lower()
    x[login] = [input("Digite o seu nome: "),
                input("Digite a ultima data de acesso: "),
                input("Digite a ultima estação acessada: ").lower()]

def busca(x):
    busca = input("Digite o login: ").lower()
    for i in x:
        if busca==i:
            print(
                "Login:.....................:",i,
                "Nome:......................:",i[0],
                "Ultima data de acesso:.....:",i[1],
                "Nome:......................:",i[2],
            )
        else:
            print("Usuario não encontrado!")