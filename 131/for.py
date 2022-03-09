# tabuada ate 100

num=int(input("Digite o numero que deseja saber a tabuada: "))

for ct in range(0,51,5):
    print(str(num) + " X " + str(ct) + " = " + str(int(num*ct)))
print("...")