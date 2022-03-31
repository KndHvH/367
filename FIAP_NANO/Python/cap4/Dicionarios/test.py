dici = {}


login = 'matias'

dici[login]=['Matias Herklotz', '22', '22']


with open("bd.txt", "r") as arquivo:
    for i in arquivo.readlines():
        print(i)

print(dici.items())