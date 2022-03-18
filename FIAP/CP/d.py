#9

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

print("Novo salario =",salario)