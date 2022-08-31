
 
lista = [2,5,8,3,8,9,5,3,5,7,3,10,4,1,0,3,2,4,11,12,4,8,5,4,3,2,1,8,7,6,4,9,8,1,2,0,6,2,0,8,4]
order = int(input("1 or -1"))


for i in range(len(lista)-1):
    for i in range(len(lista)-1):
        first = lista[i]
        if order ==1:
            if first>lista[i+1]:
                lista[i]=lista[i+1]
                lista[i+1]=first
        if order ==-1:
            if first<lista[i+1]:
                lista[i]=lista[i+1]
                lista[i+1]=first
        print(lista)