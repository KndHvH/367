import re
from random import randint

# EXERCÍCIOS:
# 1. Contar palavras
#         Testes:
#         Olá, bom dia (3)
#         Olá,bom.dia(3)
#         Olá,                bom.dia (3)
# 2. Dados 9 digitos do numero do CPF, verificar se ele é ou não válido
# 3. Dados 9 digitos do numero do CPF, apresentar os 2 dígitos correspondentes
# 4. Gerar um CPF aleatório
#     from random import randint
#     numero = str(randint(100000000, 999999999))






#1
def wordsCounter(phrase:str)->int:
    phrase = phrase.replace('.','/')
    phrase = phrase.replace(',','/')

    words = phrase.split('/')
    return len(words)

#test
print(wordsCounter("ola,             amigos.Vapo"))



#2
def caracterRemoval(phrase:str)->str:
    phrase = re.sub("\D","",phrase)
    return phrase

def firstDigitCalculator(cpf:str)->int:    
    number = 10
    total = 0
    for i in cpf:
        total += int(i)*number
        number -= 1
    if total % 11 < 2:
        return 0
    digt = 11 - (total%11)
    if digt > 9:
        return 0
    return digt
    
def secondDigitCalculator(cpf:str)->int:
    digt1 = firstDigitCalculator(cpf)
    cpf = cpf + str(digt1)
    number = 11
    total = 0
    for i in cpf:
        total += int(i)*number
        number -= 1
    if total % 11 < 2:
        return 0
    digt = 11 - (total%11)
    if digt > 9:
        return 0
    return digt

def cpfVerificator(cpf:str)->bool:
    cpf = caracterRemoval(cpf)
    cpf2 = cpf[:-2]

    dig1 = firstDigitCalculator(cpf2)
    dig2 = secondDigitCalculator(cpf2)

    cpf2 = cpf2 + str(dig1) + str(dig2)

    if cpf2 == cpf:
        return True
    return False

#test
print(cpfVerificator('168.995.350-09'))


#3
def verificationCalculator(cpf:str)->str:
    clean = caracterRemoval(cpf)


    dig1 = firstDigitCalculator(clean)
    dig2 = secondDigitCalculator(clean)

    return '-' + str(dig1) + str(dig2)

#test
print(verificationCalculator('168995350'))


#4 
def cpfGenerator(n=1)->str:
    cpfs = []
    while n > 0:
        nine = str(randint(100000000, 999999999))
        eleven = verificationCalculator(nine)
        cpf = nine[:3] + '.' + nine[3:6] + '.' +  nine[6:9] + eleven
        cpfs.append(cpf)
        n -= 1
    return cpfs

#test

cpfs = cpfGenerator(5)
print(cpfs)