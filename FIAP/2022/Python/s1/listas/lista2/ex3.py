'''
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências,
I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.
'''
kwh=int(input("Digite a quantidade de kWh consumida: "))

tipo=input("\nqual o tipo de instalação?\n" +
        "<R> - Para Residencial\n" +
        "<I> - Para Industrial\n" +
        "<C> - Para Comercial: ").upper()

total = kwh*0.4
if kwh>500:
    total = kwh * 0.65

if tipo=='C':
    total = kwh * 0.55
    if kwh>1000:
        total = kwh * 0.60

if tipo=='I':
    total = kwh * 0.55
    if kwh>5000:
        total = kwh * 0.60

print(f"\nTotal a pagar: R${total:.2f}")
