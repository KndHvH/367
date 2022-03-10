z=['z','a','e']
x=[]

for i in range(0,10,1):
    x.append(input())

print(x[0])
    #x[0]='z'
for i in range(0,10,1):
    x.append(x[i].upper())

print("T",z[2],x[0],x[5])
for i in range(0,19,1):

    for l in range(0,len(z),1):

        if z[l]==x[i]:
            #  z[2]==x[0]
            #  'z'=='z'
            if l < 10:
                if l <5:
                    print((z[l]) + "->" + (x[i + 5]))
                    z[l]=x[i+5]
                #   z[2]=x[0+5]
                #   z[2]=x[5]='p'
                else:
                    print((z[l])+"->"+(x[i-5]))
                    z[l]=x[i-5]
            else:
                if l <15:
                    print((z[l])+"->"+(x[i+5]))
                    z[l]=x[i+5]

                else:
                    print((z[l])+"->"+(x[i-5]))
                    z[l]=x[i-5]

print("T",z[2],x[0],x[5])
print(*z)
