
'''

  0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18  19
['z', 'e', 'n', 'i', 't', 'p', 'o', 'l', 'a', 'r', 'Z', 'E', 'N', 'I', 'T', 'P', 'O', 'L', 'A', 'R']
0 = 5
1 = 6
2 = 7
5 = 1

zenit
polar

'''

z=[
       #z[2]='z'
    'g','h','z','_','H','I','i','k',
    '0','v','n','k','w','B','u','U',
    'U','Z','n','y','6','e','k','S',
    '3','G','U','V','V','Z','2','k',
    'N','k','3','X','F','k','C','z',
]

x=[]

for i in range(0,10,1):
    x.append(input())

#print(x[0])
    #x[0]='z'
for i in range(0,10,1):
    x.append(x[i].upper())

#print("T",z[2],x[0],x[5])
for i in range(0,len(z),1):

    for l in range(0,19,1):

        if z[i]==x[l]:
            #  z[2]==x[0]
            #  'z'=='z'
            if l < 10:
                if l <5:
                #    print((z[i]) + "->" + (x[l + 5]))
                    z[i]=x[l+5]
                    break
                #   z[2]=x[0+5]
                #   z[2]=x[5]='p'
                else:
                #    print((z[i])+"->"+(x[l-5]))
                    z[i]=x[l-5]
                    break
            else:
                if l <15:
                #    print((z[i])+"->"+(x[l+5]))
                    z[i]=x[l+5]
                    break

                else:
                #    print((z[i])+"->"+(x[l-5]))
                    z[i]=x[l-5]
                    break

#print("T",z[2],x[0],x[5])
print(*z)



#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