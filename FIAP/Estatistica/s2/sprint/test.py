bad = 0.05

god = 0.95

total = 10
dictt = {}
while total > -1:

    chance = god ** total * bad ** (10 - total)

    print(f"chance {(10 - total)} bads = {bad ** (10 - total)}")
    print("x")
    print(f"chance {total} goods = {god ** total}")
    print("total chance =",chance)
    print("---------------------")

    dictt[10-total] = chance

    total -= 1

media = 0
for i in dictt:
    media += (i*dictt[i])
    print(f"media = {media} + ({i}*{dictt[i]})")
    
print("media total= ",media)
print("---------------------")

ex = 0

for i in dictt:
    ex += (i**2*dictt[i])
    print(f"ex = {ex} + ({i}*{dictt[i]})")
    
print("ex total = ",ex)
print("---------------------")


variancia = ex - media**2

desp = variancia**0.5

print("desvio padrao = ", desp)
print("---------------------")