
x='ghz_beB5J83pSEeV5ELq5Snfw1AIbhP53A0h2vyz'

z=list(x)

x=[]
senha=input()
x=list(senha)


for i in range(0,10):
    x.append(x[i].upper())


for i in range(0,len(z),1):
    for l in range(0,19):
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

