fita = ['delt','a','a','b','b','']
posicao = 0

#q0
x=1
while x==1:

    if fita[posicao] == 'delt':
        fita[posicao]= 'delt'
        posicao += 1

    elif fita[posicao] == 'a':
        fita[posicao]= 'A'
        posicao += 1

        #q1
        y = 1
        while y == 1:

            if fita[posicao] == 'B':
                fita[posicao] = 'B'
                posicao += 1

            elif fita[posicao] == 'a':
                fita[posicao] = 'a'
                posicao += 1

            elif fita[posicao] == 'b':
                fita[posicao] = 'B'
                posicao -= 1

    elif fita[posicao] == 'B':
        fita[posicao] = 'B'
        posicao += 1

    else:
        x=0
