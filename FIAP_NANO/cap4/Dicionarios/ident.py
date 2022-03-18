
def pergunta():
    return input("o que deseja realizar?\n" +
          "<I> - Para Inserir um usuario\n" +
          "<P> - Para Pesquisar um usuario\n" +
          "<E> - Para Excluir um usuario\n" +
          "<L> - Para Listar um usuario\n" +
          "<S> - Para Sair do programa: ").upper()

def data_input():
    return
    login = input("Digite o login: ").lower()
    usuarios[login] = [input("Digite o seu nome: "),
                 input("Digite a ultima data de acesso: "),
                 input("Digite a ultima estação acessada: ").lower()]

def busca():
    return
    busca = input("Digite o login: ").lower()