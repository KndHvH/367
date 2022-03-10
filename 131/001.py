
'''

  0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18  19
['z', 'e', 'n', 'i', 't', 'p', 'o', 'l', 'a', 'r', 'Z', 'E', 'N', 'I', 'T', 'P', 'O', 'L', 'A', 'R']
0 = 5
1 = 6
2 = 7
5 = 1


'''

z=[

    'g','h','z','_','H','I','i','k',
    '0','v','n','k','w','B','u','U',
    'U','Z','n','y','6','e','k','S',
    '3','G','U','V','V','Z','2','k',
    'N','k','3','X','F','k','C','z',
]

x=[]

for i in range(0,10,1):
    x.append(input())


for i in range(0,10,1):
    x.append(x[i].upper())


for i in range(0,len(z),1):

    for l in range(0,19,1):

        if z[i]==x[l]:

            if l < 10:
                if l <5:

                    z[i]=x[l+5]
                    break

                else:

                    z[i]=x[l-5]
                    break
            else:
                if l <15:

                    z[i]=x[l+5]
                    break

                else:

                    z[i]=x[l-5]
                    break


print(*z)

y=str(z)
print(z.replace(" ", ""))




