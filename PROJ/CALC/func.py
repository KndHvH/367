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
    opera = 'x'
    while x == 1:
        opera = operacao()
        print(opera)
        if opera == 'S' or opera == 'U' or opera == 'D' or opera == 'M' or opera == 'E':
            x = 0
        else:
            print("Operação invalida!\n")
            x = 1


def conta():
    if opera == 'S':
        resultado = n1 + n2
        simb='+'
    elif opera == 'U':
        resultado = n1 - n2
        simb='-'
    elif opera == 'D':
        resultado = n1 / n2
        simb='/'
    elif opera == 'M':
        resultado = n1 * n2
        simb='*'
    else:
        return 0
