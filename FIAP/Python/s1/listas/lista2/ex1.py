
'''
Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular soma,
subtração, multiplicação e divisão. Exiba o resultado da operação
solicitada.

'''

n1=int(input("Digite o primeiro numero: "))

simb=input("\no que deseja realizar?\n" +
        "<+> - Para Somar\n" +
        "<-> - Para Subtrair\n" +
        "</> - Para Dividir\n" +
        "<*> - Para Multiplicar: "\
         ).upper()

n2=int(input("\nDigite o proximo numero: "))

if simb == '+':
    resultado = n1 + n2
elif simb == '-':
    resultado = n1 - n2
elif simb == '/':
    resultado = n1 / n2
else:
    resultado = n1 * n2

print(f"\nResultado de:\n {n1} {simb} {n2} = {resultado}\n")