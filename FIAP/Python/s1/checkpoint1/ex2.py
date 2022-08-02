
anterior = float(input("Digite a leitura do mes anterior: "))
atual = float(input("Digite a leitura do mes atual: "))

consumo_mensal = atual - anterior

tusd = consumo_mensal * 0.40942
te = consumo_mensal * 0.38317
pis = consumo_mensal * 0.01
cofins  = consumo_mensal * 0.0462

total_a_pagar = tusd + te + pis + cofins

print(f"Consumo do mes (kWh) = {consumo_mensal:.2f}")
print(f"TUSD = R$ {tusd:.2f}")
print(f"TE = R$ {te:.2f}")
print(f"PIS/PASEP = R$ {pis:.2f}")
print(f"COFINS = R$ {cofins:.2f}")
print(f"Total a pagar (R$) = {total_a_pagar:.2f}")
