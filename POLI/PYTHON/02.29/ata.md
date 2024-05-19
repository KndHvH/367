Primeira aula Pyton, Professor thiago martins 
(branco, moreno semi grisalio estatura media e cavanhaque)

Resumo inicial de como serao as aulas, explicando que para as proximas 5 aulas serao de conteudo e exercicios


Primeira aula sobre python, falou das variaveis, tipos de dados, como python interpreta, como armazena informacoes, operacoes logicas e matematicas.

Realmente correu bastante com o conteudo, coitado de quem comecou a programar hoje

Ja saiu na lata com indexacao de lista, mostrando funcoes etc, nao entrou no detalhe da funcao, mas so faltava ne kkkkkkkkkkkkkk

mostrou algumas curiosidades e informacoes sobre outras linguagens, mas ate agora nada novo de baixo do sol

Variaveis sao referencias na memoria, ponteiros...

Ex:

a = [1,2,'tres']

Memoria

a -> [ o , o , o ]
       |   |   |
       1   2  'tres'       

Um inteiro e imutavel, pois ao fazer somas ou modificacoes, criamos um novo local na memoria para armazenar o resultado, e mudamos o apontamento, o mesmo nao ocorre com lista que sao mutaveis, 


>>> 'zz' < 'abc'
False
>>> 'ab' < 'abc' 
True
>>> [1,2,3] + 4  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "int") to list
>>> [1,2,3] + [4] 
[1, 2, 3, 4]


>>> b = a
>>> a.append(5)
>>> b
[1, 2, 3, 4, 5]

