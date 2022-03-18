from ident import *
usuarios = {}

opcao = input("o que deseja realizar?\n" +
          "<I> - Para Inserir um usuario\n" +
          "<P> - Para Pesquisar um usuario\n" +
          "<E> - Para Excluir um usuario\n" +
          "<L> - Para Listar um usuario: ").upper()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        login=input("Digite o login: ").upper()
        nome=input("Digite o seu nome: ").upper()
        data=input("Digite a ultima data de acesso: ").upper()
        estacao=input("Digite a ultima estação acessada: ").upper()
        usuarios[login]=[nome,data,estacao]

    opcao = input("o que deseja realizar?\n" +
                  "<I> - Para Inserir um usuario\n" +
                  "<P> - Para Pesquisar um usuario\n" +
                  "<E> - Para Excluir um usuario\n" +
                  "<L> - Para Listar um usuario: ").upper()