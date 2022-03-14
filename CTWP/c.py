#6

distancia=int(input("Digite a distancia da viagem em km: "))
vmedia=int(input("Digite a velocidade media prevista em km/h: "))

tempo=distancia/vmedia

print(f"Tempo previsto de viagem: {tempo} horas.")


print("_______________________")
#7

c=int(input("Digite a temperatura em celsius: "))

f = float(c*1.8 + 32)

print(f"Temperatura em Fahrenheit: {f}")


print("_______________________")
#8

km=int(input("Digite a qnt de KM percorrido: "))
dias=int(input("Digite a qnt de dias alugado: "))

val_km=km*0.15
val_dias=dias*60

total=val_km+val_dias

print("Total gasto: R$",total)

=teste