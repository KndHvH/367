km=float(input("Digite a quantidade de Km: "))
passagem = km * 0.5
if km>200:
    passagem = km * 0.45
print(f"O valor da passagem é de: R${passagem:.2f}")