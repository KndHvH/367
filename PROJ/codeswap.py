
import random
import re


def main():

    while True:

        choice = decision()

        if choice == 'a':
            master = list(input('file: '))
            password = password_verif()

            master = swap(master,password)

            print(list_to_string(master))

    



def decision() -> str:
    """
    permite ao usuario escolher o que deseja fazer no programa
    e retorna sua decisao

    @return: sua decisao entre a / c
    """
    while True:
        try:
            print('a: add | s: swap')
            choice = input(": ").lower()

            if choice != 'a' and choice != 's':
                raise ValueError

            return choice

        except ValueError:
            print("error!")


def password_verif() -> str:
    while True:
        try:
            password = input("password: ").lower()

            if len(password) % 2 != 0:
                print('password size can\'t be even.')
                raise ValueError

            if len(password) < 4:
                print('password too small.')
                raise ValueError

            if re.search('\W', password):
                print('password can only contain letters.')
                raise ValueError

            if has_double(password):
                print('password can\'t have repeated letters.')
                raise ValueError


            upper = password.upper()
            password = password + upper
            return password

        except ValueError:
            print('error!')


def has_double(string: str) -> bool:
    stringlist = list(string)

    if len(stringlist) != len(set(stringlist)):
        return True
    return False


def swap(master: list, senha: list) -> list:
    step = int(len(senha)/4)
    for i, v in enumerate(master):
        for j, b in enumerate(senha):
            if v == b:
                if j < 5 or (j > 9 and j < 15):
                    master[i] = senha[j+step]
                else:
                    master[i] = senha[j-step]
    return master


def list_to_string(list: list) -> str:
    string = ""
    for i in list:
        string += i
    return string


if __name__ == '__main__':
    main()
