# Matias Herklotz - rm94199

def main():

    notas = {}

    while True:

        opcoes()

        escolha = choice()

        match escolha:

            case 0:
                break

            case 1:
                notasCadastro(notas)

            case 2:
                printGrades(notas)


def printGrades(notas: dict):
    """mostra as 

    Args:
        notas (dict): recebe o dicionario de notas para poder printar
    """
    if notas != {}:
        print('')
        print('DISCIPLINAS | NOTA | STATUS')
        print('--------------------')
        for i in notas:
            print(f'{i} | {notas[i][0]} | {notas[i][1]}')
    else:
        print('materias nao cadastradas!')


def notasCadastro(notas: dict) -> dict:
    """funcao para cadastrar as notas

    Args:
        notas (dict): recebe o dicionario de notas e pede ao usuario inserir mais notas

    Returns:
        dict: dicionario de notas
    """
    print('')
    print('CADASTRAR NOTAS')
    print('Digite \'.\' em diciplina para sair!')
    print('--------------------')

    while True:
        print('')
        disc = input('Disciplina.....: ')
        if disc == '.':

            return notas

        media = int(input('Media anual....: '))
        status = gradeStatus(media)

        notas[disc] = [media, status]


def gradeStatus(nota: int) -> str:
    """verifica o status da materia com base na media anual

    Args:
        nota (int): nota da disciplina

    Returns:
        str: retorna se foi aprovado ou reprovado
    """
    if nota >= 6:
        return 'Aprovado'
    return 'Reprovado'


def opcoes():
    """printa as opcoes do menu
    """
    print('CADASTRO DISCIPLINAS')
    print('--------------------')
    print('0 - SAIR')
    print('1 - Cadastrar notas')
    print('2 - Listar registro completo')
    print('')


def choice() -> int:
    """pede ao usuario que escolha o que fazer

    Raises:
        ValueError: caso o numero inserido nao seja um numero ou diferente de 0,1,2 , o programa pede para tentar de novo

    Returns:
        int: retorna a escolha do usuario
    """
    while True:

        try:
            choice = int(input('Opcao desejada: '))
            if choice > 2 or choice < 0:
                raise ValueError
            return choice

        except ValueError:
            print("Favor Digitar um numero Valido!")


if __name__ == '__main__':
    main()
