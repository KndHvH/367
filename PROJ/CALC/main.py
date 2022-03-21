from func import *

n1=int(input("Digite o primeiro numero: "))

j=1
while j==1:
    i = 1
    while i == 1:
        letra = operacao()
        i = verif(letra)

    n2=int(input("Digite o proximo numero: "))

    resultado=conta(letra,n1,n2)
    simb=simbolo(letra)

    print(f"Resultado de:\n {n1} {simb} {n2} = {resultado}")

    i = 1
    while i == 1:
        letra2=decisao()
        i = verif2(letra2)


'''    j='''

