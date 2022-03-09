
'''

zenit
polar

ghz_WbhVNhOLLo1omDJDauktkXt2l5jVtB0rifzf
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
  0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18  19
['z', 'e', 'n', 'i', 't', 'p', 'o', 'l', 'a', 'r', 'Z', 'E', 'N', 'I', 'T', 'P', 'O', 'L', 'A', 'R']
0 = 5
1 = 6
2 = 7
5 = 1

'''

z=[
    'g','h','z','_','W','b','h','V','N',
    'h','O','L','L','o','1','o','m','D',
    'J','D','a','u','k','t','k','X','t',
    '2','l','5','j','V','t','B','0','r',
    'i','f','z','f'
]
x=[]
print(*z)

for i in range(0,10,1):
   x.append(input())

for i in range(0,10,1):
   x.append(x[i].upper())

for i in range(0,len(z)):
    for l in range(0,len(x)):
        if z[i]==x[l]:
            if l < 10:
                if l <5:
                    z[i]=x[l+5]
                else:
                    z[i]=x[l-5]
            else:
                if l <15:
                    z[i]=x[l+5]
                else:
                    z[i]=x[l-5]

print(*z)




