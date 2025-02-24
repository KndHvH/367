# https://drive.google.com/file/d/1LHXQyuXlQza0VZ8xONvYS4r7c6-qTm43/view?usp=sharing

# Cesar Norena Pachon - RM95093
# Eduardo Matos da Silva - RM92877
# Matias Cornelsen Herklotz - RM94199
# Tabatha Larissa Alves de Souza - RM93045

import random


def main():
    print("-----------------------")
    print("MENU - OusadIA")

    comments = importData()

    while True:

        choice = decision()

        if choice == 0:
            saveData(comments)
            break

        if choice == 1:
            comments = insertData(comments)

        if choice == 2:
            comments = convertData(comments)

        if choice == 3:
            showData(comments)

        if choice == 4:
            sortById(comments)

        if choice == 5:
            sortByScore(comments)

        if choice == 6:
            comments = []
            saveData(comments)


def insertData(comments: list) -> list:
    """
    recebe a lista de comentarios ja existentes e pede ao usuario que ele insira novas entradas
    e retorna a lista com todos os comentarios


    @param: lista de comentarios

    @return: nova lista de comentarios
    """
    i = len(comments)
    while True:
        comment = input(
            f'Digite o comentario numero {i+1} (digite 0 para sair): ')
        if comment == '0':
            return comments
        comments.append({"id": i, "comentario": comment, 'score': None})
        i += 1


def showData(comments: list):
    """
    recebe a lista de comentarios ja existentes e mostra ao usuario

    @param: lista de comentarios
    """
    print("-----------------------")
    if comments == []:
        print('Não foram inseridos comentarios!')
    else:
        for i in comments:
            print(f"Comentario #{i['id']+1}: {i['comentario']}." +
                  (i['score'] != None and f"\nScore: {i['score']}" or ""))


def convertData(comments: list) -> list:
    """
    atribui uma nota de 0 a 5 baseado no comentario do cliente,
    escolhidos aleatoriamente *

    @param: dicionario de commentarios

    @return: dicionario de comentarios
    """
    if comments == []:
        print("-----------------------")
        print('Não foram inseridos comentarios!')

        return comments
    for i in comments:
        numero = random.randrange(0, 6)
        if i['score'] == None:
            i['score'] = numero
    print("-----------------------")
    print('Comentarios convertidos!')
    return comments


def decision() -> int:
    """
    permite ao usuario escolher o que deseja fazer no programa
    e retorna sua decisao

    @return: sua decisao entre 0-6
    """
    while True:
        try:
            menuDisplay()
            choice = int(
                input("Digite o numero do procedimento que deseja realizar: "))

            if choice > 6 or choice < 0:
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
    print("4 - Ordenar lista por Id")
    print("5 - Ordenar lista por Score")
    print("6 - Apagar lista")
    print("0 - SAIR")


def saveData(list: list):
    """armazena a lista de dicionarios em um arquivo txt

    Args:
        list (list): lista de dicionarios
    """
    with open("db.txt", "w") as db:

        for db_dict in list:

            db.write(f"{str(db_dict)}\n")


def importData() -> list:
    """importa a lista pelo txt e retorna a lista

    Returns:
        list: lista de dicionarios de comentarios
    """
    try:
        with open("db.txt", "r") as db:
            db_list = []
            for line in db:
                db_list.append(eval(line))

    except FileNotFoundError:
        db_list = []

    return db_list


def sortByScore(comments: list) -> list:
    """organiza a lista de comentarios pelo score do sentimento em ordem crescente

    Args:
        comments (list): lista de comentarios

    Returns:
        list: lista de comentarios organizada
    """
    for i in comments:
        if i['score'] == None:
            print("-----------------------")
            print('Nem todos os comentarios receberam um Score!')
            return None
    comments.sort(key=getScore)


def getScore(e: dict) -> int:
    """funcao para retornar score de um comentario

    Args:
        e (dict): comentario

    Returns:
        int: score do comentario
    """
    return e['score']


def sortById(comments: list) -> list:
    """organiza a lista de comentarios em ordem de ID

    Args:
        comments (list): lista de comentarios

    Returns:
        list: lista de comemtarios organizada
    """
    comments.sort(key=getId)


def getId(e: dict) -> int:
    """funcao para retornar id de um comentario

    Args:
        e (dict): comentario

    Returns:
        int: id do comentario
    """
    return e['id']


if __name__ == '__main__':
    main()
