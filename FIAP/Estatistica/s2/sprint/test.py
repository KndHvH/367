bad = 0.05
god = 0.95
total = 10
popam = total
dictt = {}
while total > -1:

    chance = god ** total * bad ** (popam - total)

    print(f"chance {(popam - total)} bads = {bad ** (popam - total)}")
    print(f"chance {total} goods = {god ** total}")
    print("total chance =",chance)
    print("---------------------")

    dictt[popam-total] = chance

    total -= 1

media = 0
for i in dictt:
    
    print(f"media = {media} + ({i}*{dictt[i]})")
    media += (i*dictt[i])
    
print("media total= ",media)
print("---------------------")

ex = 0

for i in dictt:
    
    print(f"ex = {ex} + ({i}*{dictt[i]})")
    ex += (i**2*dictt[i])
    
print("ex total = ",ex)
print("---------------------")


variancia = ex - media**2

desp = variancia**0.5

print("desvio padrao = ", desp)
print("---------------------")

verif = 0

for i in dictt.keys():
    verif += dictt[i]

print("verif = ",verif)
print("---------------------")