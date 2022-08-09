# calcular a media final de um aluno FIAP



def main():

    semestre1 = inputData(1)
    notaSem1 = calcAll(semestre1)
    

    semestre2 = inputData(2)
    notaSem2 = calcAll(semestre2)


    notaTotal = (notaSem1*0.4 + notaSem2*0.6)


    status = setStatus(notaTotal)


    if status == "Prova EXAME!":
        print("Necessario Exame!")
        status = exame(notaTotal)

    
    print("Status:",status)

def inputData(n):
    """
    recebe todos os inputs e armazena em uma lista

    @param param1: o numero do semestre
    @return: retorna a lista de notas
    """
    print(f"Semestre:{n} ")

    notas = []
    for i in range(1,4):
        nota = int(input(f"Digite a nota do Checkpoint{i}: "))
        notas.append(nota)
    for i in range(1,3):
        nota = int(input(f"Digite a nota do Sprint{i}: "))
        notas.append(nota)
    nota = int(input(f"Digite a nota do GS: "))
    notas.append(nota)

    return notas

def calcCheck(lista):
    """
    calcula a media dos checkpoins e exclui o de menor nota

    @param param1: lista das notas
    @return: retorna a media dos checkpoints
    """
    totalCheck = 0
    menor = 100000
    for i in range (0,3):
        totalCheck += lista[i]
        if lista[i] < menor:
            menor = lista[i]
    return (totalCheck - menor)/2


def calcSprint(lista):
    """
    calcula a media das sprints

    @param : lista de notas
    @return: retorna a media dos 2 sprints
    """
    return (lista[3] + lista[4]) / 2

def pesoNota(check,sprint,gs):
    """
    calcula a nota do semestre com a media de todas as avaliacoes

    @param param1: media dos 2 maiores checkpoints
    @param param2: media dos 2 sprints
    @param param3: nota globalsolution
    @return: retorna a nota do semestre
    """
    a = (check+sprint)*0.2
    b = gs*0.6
    return (a+b)


def calcAll(lista):
    """
    recebe o input de todas as notas e chama todas as outras funcoes do codigo para realizar os calculos
    de media e status de cada tipo de avaliacao

    @param lista das notas de um semestre
    @return: retorna a nota do semestre
    """
    checkSem = calcCheck(lista)
    sprintSem = calcSprint(lista)
    gsSem = lista[5]
    notaSem = pesoNota(checkSem, sprintSem, gsSem)

    print("Media Sprint:", sprintSem)
    print("Media GS:", gsSem)
    print("Media Semestre:", notaSem)
    return notaSem

def setStatus(nota):
    """
    Define o status do estudante com base na sua nota final do ano

    @param param1: nota final do ano
    @return: retorna o status do aluno
    """
    status = "Reprovado!"
    if nota >= 6:
        status = "Aprovado!"
    elif nota >= 4:
        status = "Prova EXAME!"
    return status



def exame(notaTotal):
    """
    funcao para receber a nota do exame e calcular o novo status do aluno

    @param Nota total do ano
    @return: retorna o novo status do aluno
    """

    status = "Reprovado em EXAME"
    notaExame = int(input("Digite a nota do exame: "))
    if (notaTotal+notaExame)/2 >= 6:
        status = "Aprovado em EXAME"
    return status


if __name__ == '__main__':
    main()



"""
describe

@param param1: this is a first param
@param param2: this is a second param
@return: this is a description of what is returned
@raise keyError: raises an exception
"""