import itertools


class ConjuntoVariaveis():
    def __init__(self,variaveis:list,probabilidades:list) -> None:
        self._variaveis = variaveis
        self._probabilidades = probabilidades
        self._conjunto = zip(variaveis,probabilidades)
    
    def __iter__(self):
        return iter(self._conjunto)

class CalculaProbabilidade():
    @staticmethod
    def simples(evento, espaco):
        return evento/len(espaco)

    @staticmethod
    def distribuicao(conjunto:ConjuntoVariaveis, choice, n_evento):
        probabilidade_choice = [[i] for i in range(n_evento)+1]
        probabilidades = []
        combinacoes = [comb for comb in itertools.product(conjunto._variaveis,repeat=n_evento)]
        for comb in combinacoes:
            probabilidade_local = 1
            for letter in comb:
                probabilidade_local *= conjunto._probabilidades[conjunto._variaveis.index(letter)]
            print("".join(comb),probabilidade_local)
            
            if choice in "".join(comb):
                probabilidade_choice += probabilidade_local
        print(f"Probabilidade de {choice}: {probabilidade_choice}")
        
        
probabilidade = CalculaProbabilidade.distribuicao(ConjuntoVariaveis(['D','B'],[0.6,0.4]),"D",3)
            