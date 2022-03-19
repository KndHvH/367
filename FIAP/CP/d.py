'''#9

loop=1
while loop==1:
    x=int(input("Digite o valor de X: "))
    y=int(input("Digite o valor de Y: "))
    if x==y:
        print("Os numeros nao podem ser iguais!")
        loop=1
    else:
        loop=0

z= (x**2 + y**2) / (x-y)**2

print("Valor de Z =",z)


####################################
#10

salario=float(input("Digite o valor do salario: "))

salario=salario*1.35

print("Novo salario =",salario)'''


'''a=int(input("Digite um numero: "))
b=int(input("Digite um numero: "))
c=int(input("Digite um numero: "))

if a > b:
    if c > a:
        print("Maior numero:",c)
    if c < a:
        print("Maior numero:", a)
if a < b:
    if c > b:
        print("Maior numero:",c)
    if c < b:
        print("Maior numero:", b)'''