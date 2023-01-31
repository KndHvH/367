fita = ['delt','a','a','b','b','']
posicao = 0
movimento = 1
print(fita, movimento)


#q0
q0=1
while q0==1:

    if fita[posicao] == 'delt':
        fita[posicao]= 'delt'
        posicao += 1
        movimento +=1
        print(fita,movimento)

    elif fita[posicao] == 'a':
        fita[posicao]= 'A'
        posicao += 1
        movimento +=1
        print(fita,movimento)

        #q1
        q1 = 1
        while q1 == 1:

            if fita[posicao] == 'B':
                fita[posicao] = 'B'
                posicao += 1
                movimento += 1
                print(fita, movimento)

            elif fita[posicao] == 'a':
                fita[posicao] = 'a'
                posicao += 1
                movimento += 1
                print(fita, movimento)

            elif fita[posicao] == 'b':
                fita[posicao] = 'B'
                posicao -= 1
                movimento += 1
                print(fita, movimento)

                #q2
                q2 = 1
                while q2 == 1:

                    if fita[posicao] == 'B':
                        fita[posicao] = 'B'
                        posicao -= 1
                        movimento += 1
                        print(fita, movimento)

                    elif fita[posicao] == 'a':
                        fita[posicao] = 'a'
                        posicao -= 1
                        movimento += 1
                        print(fita, movimento)

                    elif fita[posicao] == 'A':
                        fita[posicao] = 'A'
                        posicao += 1
                        movimento += 1
                        print(fita, movimento)
                        q2=0
                        q1=0



    elif fita[posicao] == 'B':
        fita[posicao] = 'B'
        posicao += 1
        movimento +=1
        print(fita,movimento)

    else:
        x=0
