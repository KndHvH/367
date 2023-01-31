# Segunda versao, adaptando antigo programa para atender as necessidades do sprint3
import random


def main():
    print("-----------------------")
    print("MENU - OusadIA")

    comments = {}

    while True:
    
        choice = decision()

        if choice == 0: 
            break

        if choice == 1: 
            comments = insertData(comments)

        if choice == 2: 
            comments = dataConvert(comments)

        if choice == 3: 
            showData(comments)   

    
def insertData(comments:dict)->dict:
    """
    recebe a lista de comentarios ja existentes e pede ao usuario que ele insira novas entradas
    e retorna a lista com todos os comentarios

    @param: lista de comentarios

    @return: nova lista de comentarios
    """
    i = len(comments) + 1
    while True:
        comment = input(f'Digite o comentario numero {i} (digite 0 para sair): ')
        if comment == '0':
            return comments
        comments[i] = [comment]
        i+=1


def showData(comments:dict):
    """
    recebe a dicionario de comentarios ja existentes e mostra ao usuario

    @param: dicionario de comentarios
    """
    if comments == {}:
        print("-----------------------")
        print('Não foram inseridos comentarios!')
    else:
        print("-----------------------")
        for i in comments.keys():
            print(f"Comentario #{i}: {comments[i][0]}." + (len(comments[i]) == 2 and f"\nScore: {comments[i][1]}" or ""))


def dataConvert(comments:dict)->dict:
    """
    atribui uma nota de 0 a 5 baseado no comentario do cliente,
    escolhidos aleatoriamente *

    @param: dicionario de commentarios

    @return: dicionario de comentarios
    """
    if comments == {}:
        print("-----------------------")
        print('Não foram inseridos comentarios!')
    else:  
        for i in comments.keys():
            numero = random.randrange(0,6)
            if len(comments[i])==1:
                comments[i].append(numero)
        print("-----------------------")
        print('Comentarios convertidos!')
        return comments


def decision()->int:
    """
    permite ao usuario escolher o que deseja fazer no programa
    e retorna sua decisao

    @return: sua decisao entre 0-3
    """
    while True:
        try:
            menuDisplay()
            choice = int(input("Digite o numero do procedimento que deseja realizar: "))

            if choice > 3 or choice < 0:
                raise ValueError

            return choice

        except ValueError:
            print("-----------------------")
            print('Favor inserir numero valido!')



def menuDisplay():
    """
    mostra as opções do menu
    """
    print("-----------------------")
    print("1 - Inserir comentarios do clientes")
    print("2 - Converter dados quali. para quant.")
    print("3 - Exibir todos os comentarios")
    print("0 - SAIR")


if __name__ == '__main__':
    main()


