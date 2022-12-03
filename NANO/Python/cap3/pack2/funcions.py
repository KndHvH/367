def f(x):
    return x**2 + 1

def gmail_gen(bd):
    return bd + '@gmail.com'

def letra1(n1,n2):
    if n1[0]==n2[0]:
        return "Mesmas iniciais"
    else:
        return "Iniciais diferentes"

def inboth(wd1,wd2):
    "Takes two strings, returns a sorted list of common characters"
    common=[]
    for i in wd1:
        if i in wd2:
            common.append(i)
    common=list(dict.fromkeys(common))

    return sorted(common)
