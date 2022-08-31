# Sabemos que um triângulo tem 3 lados.
# Para ser um triangulo um lado deve ser menor que a soma dos outros dois, nas 3 óticas.
# Caso tenhamos certeza que os lados formam um triângulo, temos que decidir de qual tipo é este triângulo. Seguem os critérios:
# - Equilátero: os três lados são iguais.
# - Isósceles: 2 lados são iguais.
# - Escaleno: 3 lados diferentes.
# Crie uma solução que pegue três valores fornecidos pelo usuário e diga, se for um triângulo, qual ele é.
# A cada verificação, pergunte se o usuário deseja continuar executando o programa, sendo 1 para Sim ou 2 para Não. Números diferentes deste, advertir e pedir um destes números.
# Esta solução deve ser desenvolvida com o conceito de subalgoritmos onde for possível, lembrando que cada subalgoritmo deve ser atômico, ou seja, cada um resolve um problema.





def main():

    while True:

        lados = getSides()

        if triangleMatch(lados):
            tipo = triangleType(lados)
            if tipo == 1:
                print("É um triangulo Equilátero!")
            elif tipo == 2:
                print("É um triangulo Isósceles!")
            else:
                print("É um triangulo Escaleno!")

        else:
            print("Objeto inserido não é um triangulo!")

        if decision() == 2:
            break



def getSides():
    """
    recebe os 3 lados do triangulo via input e armazena em uma lista

    @return: retorna a lista de lados
    """
    while True:
        try:
            lados = []
            for i in range(0,3):
                lado = float(input(f"Digite o lado numero {i+1}: "))
                lados.append(lado)
            return lados
        except ValueError:
            print("Favor digitar um Numero! ")
        

def triangleMatch(lista):
    """
    recebe a lista de lados e verifica se é um triangulo
    (verifica se algum lado é maior que a soma dos outros 2)

    @param param1: lista de lados

    @return: True caso seja um triangulo ou False caso nao seja
    """
    total = 0
    for lado in lista:
        total += lado

    for i in range(0,3):
        if lista[i] > (total - lista[i]):
            return False
    return True
   

def decision():
    """
    pergunta ao usuario se quer recomecar o programa, e verifica se a resposta é 1 ou 2

    @return: retorna a decisao
    """
    while True:
        try:
            decision = int(input("Deseja consultar outro objeto? (1:sim/2:nao) "))
            if decision != 1 and decision != 2:
                raise ValueDiferentError
            return decision
        except ValueDiferentError:
            print("Favor digitar 1 ou 2!")
        except ValueError:
            print("Favor digitar 1 ou 2!")


def triangleType(list):
    """
    recebe a lista de lados e verifica qual tipo é o triangulo
    (verifica se algum lado é igual ao outro )

    @param param1: lista de lados

    @return: 1 ou 2 ou 3 (equilatero, isoceles, escaleno)
    """
    if list[0] == list[1] and list[1] == list[2]:
        return 1
    if list[0] == list[1] or list[0] == list[2] or list[1] == list[2]:
        return 2
    return 3

    
def eEquilatero(data : list) -> bool :
    return len(set(data)) == 1

def eEscaleno(data : list) -> bool :
    return len(set(data)) == 3

def eIsosceles(data : list) -> bool :
    return len(set(data)) == 2


class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueDiferentError(Error):
    """Raised when the input value is diferent from 1 or 2"""
    pass


if _name_ == '_main_':
    main()