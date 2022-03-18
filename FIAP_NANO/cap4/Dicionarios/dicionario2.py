from ident import *
usuarios = {}
opcao=[]
print(opcao)

decisao(opcao)


while opcao[0]=="I" or opcao[0]=="P" or opcao[0]=="E" or opcao[0]=="L":
    if opcao[0]=="I":
        login=input("Digite o login: ").upper()
        nome=input("Digite o seu nome: ").upper()
        data=input("Digite a ultima data de acesso: ").upper()
        estacao=input("Digite a ultima estação acessada: ").upper()
        usuarios[login]=[nome,data,estacao]
    decisao(opcao)