# tabuada ate 50

num=int(input("Digite o numero que deseja saber a tabuada: "))

for ct in range(0,51,1):
    print(str(num) + " X " + str(ct) + " = " + str(int(num*ct)))
print("...")


g1=[]

for i in range(0,3,1):

    g1.append(i)

for i in g1:
    print(g1,i+1)