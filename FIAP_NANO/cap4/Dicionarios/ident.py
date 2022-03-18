def decisao(a):
    b = input("o que deseja realizar?\n" +
                  "<I> - Para Inserir um usuario\n" +
                  "<P> - Para Pesquisar um usuario\n" +
                  "<E> - Para Excluir um usuario\n" +
                  "<L> - Para Listar um usuario: ").upper()
    a.append(b)