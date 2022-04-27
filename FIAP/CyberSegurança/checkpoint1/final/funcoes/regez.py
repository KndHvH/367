
def regexlist(lista):

    a='(?i)'

    for i in lista:
        a += f"({i})|"

    a = a[:-1]

    return a