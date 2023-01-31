# 4 - Dado um número, verificar se ele é primo ou não
# ENTRADA: 11	SAÍDA: É primo

x = int(input("Digite um numero: "))
contador = 0

for i in range (2,x):
    if x % i == 0:
        print(f"{x} pode ser dividido por {i}")
        contador += 1

if contador >0:
    print("Numero nao e primo")
else:
    print("Numero e primo")
