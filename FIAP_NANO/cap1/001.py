
z=[
    'g','h','z','_','G','c','W','P',
    'q','8','9','H','P','g','m','C',
    '3','r','W','g','x','k','o','r',
    'H','T','J','y','I','Y','G','i',
    '9','L','1','1','e','0','6','m',
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
y=""
for i in z:
    y += i
print(y)

