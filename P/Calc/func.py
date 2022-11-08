def operacao():
    return input("\no que deseja realizar?\n" +
        "<S> - Para Somar\n" +
        "<U> - Para Subtrair\n" +
        "<D> - Para Dividir\n" +
        "<M> - Para Multiplicar: "\
         ).upper()

def verif(letra):

    if letra == 'S' or letra == 'U' or letra == 'D' or letra == 'M':
        return 0
    else:
        print("Operação invalida!\n")
        return 1


def verif2(letra):
    if letra == 'C' or letra == 'N' or letra == 'S':
        return 0
    else:
        print("Decisão invalida!\n")
        return 1

def conta(l,n1,n2):
    if l == 'S':
        return n1 + n2
    elif l == 'U':
        return n1 - n2
    elif l == 'D':
        return n1 / n2
    else:
        return n1 * n2


def simbolo(l):
    if l == 'S':
        return '+'
    elif l == 'U':
        return '-'
    elif l == 'D':
        return '/'
    else:
        return '*'

def decisao():
    return input("o que deseja realizar?\n" +
        "<C> - Para Continuar a conta\n" +
        "<N> - Para Fazer uma nova conta\n" +
        "<S> - Para Sair: ").upper()



