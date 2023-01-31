#3
def saudacao5(hora = 11, nome = "Edson"):
    if hora > 6 and hora < 13:
        saud = "Bom dia"
    elif hora > 12 and hora < 18:
        saud = "Boa tarde"
    else:
        saud="Boa noite"
    return print(f"{saud} {nome}! Seja bem vindo a FIAP")

saudacao5()

saudacao5(18,input("Digite o seu nome: "))