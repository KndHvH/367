
lista=["a","b"]

lol='(?i)'

for i in lista:
    lol += f"({i})|"

lol = lol[:-1]

print(lol)