def operacao():
    return input("o que deseja realizar?\n" +
        "<S> - Para Somar 2 numeros\n" +
        "<U> - Para Subtrair 2 numeros\n" +
        "<D> - Para Dividir 2 numeros\n" +
        "<M> - Para Multiplicar 2 numeros: "\
         ).upper()

def verif(letra):

        if letra == 'S' or letra == 'U' or letra == 'D' or letra == 'M':
            return 0
        else:
            print("Operação invalida!\n")
            return 1


def conta(l):
    if l == 'S':
        resultado = n1 + n2
        return '+'
    elif l == 'U':
        resultado = n1 - n2
        return '-'
    elif l == 'D':
        resultado = n1 / n2
        return '/'
    else:
        resultado = n1 * n2
        return '*'

