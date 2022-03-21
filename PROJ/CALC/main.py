from func import *
resultado=0

n1=int(input("Digite o primeiro numero: "))

x = 1
while x == 1:
    letra = operacao()
    x = verif(letra)

n2=int(input("Digite o proximo numero: "))

simb=conta(letra,n1,n2)

print(f"Resultado de:\n {n1} {simb} {n2} = {resultado}")