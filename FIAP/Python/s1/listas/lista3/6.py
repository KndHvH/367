#dado a base e o expoente, calcular a potencia

base = float(input("Digite a base: "))
expo = float(input("Digite o expoente: "))

total = 1.0

# if expo % 1 != 0:


if expo != 0:
    total = base
    while expo > 1:
        total *= base
        expo -= 1

    while expo < -1:
        total *= base
        expo += 1

if expo < 0:
    total = 1/total

print("Total:",total)