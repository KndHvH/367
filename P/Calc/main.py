from func import *


l=1
while l==1:

    n1=int(input("Digite o primeiro numero: "))

    j = 1
    while j==1:
        i = 1
        while i == 1:
            letra = operacao()
            i = verif(letra)

        n2=int(input("\nDigite o proximo numero: "))

        resultado=conta(letra,n1,n2)
        simb=simbolo(letra)

        print(f"\nResultado de:\n {n1} {simb} {n2} = {resultado}\n")

        i = 1
        while i == 1:
            letra2=decisao()
            i = verif2(letra2)

        j=0
        if letra2 == 'C':
            j=1
            n1=resultado
    l=0
    if letra2 == 'N':
        l=1
print(f"Resultado : {resultado:.2f}")





