def operacao():
    return input("o que deseja realizar?\n" +
        "<S> - Para Somar 2 numeros\n" +
        "<U> - Para Subtrair 2 numeros\n" +
        "<D> - Para Dividir 2 numeros\n" +
        "<M> - Para Multiplicar 2 numeros\n" +
        "<E> - Para Sair do programa: "\
         ).upper()

def verif():
    x = 1
    while x == 1:
        ope = operacao()
        if ope == 'S' or ope == 'U' or ope == 'D' or ope == 'M' or ope == 'E':
            x = 0
        else:
            print("Operação invalida!\n")
            x = 1


def conta():
    if ope == 'S':
        resultado = n1 + n2
    elif ope == 'U'
