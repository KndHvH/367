# Datawarehouse

Visa solucionar os seguintes problemas:
- Diversos problemas podem ocorrer quando não tomamos cuidado em extrair informações das empresas;
- Temos departamentos que olham valores dos mesmos indicadores de maneiras distintas;
- Diferentes formas de agregação dentro da empresa;
- Sistemas de informação que não se falam também é um problema muito comum.

Como?
Fornecendo informações gerenciais na tomada de decisões

## Caracteristicas do Datawarehouse

- Funciona separado da estrutura operacional da empresa
- Integração de diversas fontes de dados. (independente de origem, tipo ou formato ou origem interna ou externa)
- Implementeção das regras de negócio (nefinir o conceito utilizado para cada termo)
- Não possui obrigacao fiscal ou de impostos, entao pode ser modelado a gosto da empresa. 
- Limpeza de dados
- Análise ao longo do tempo (estudo do dado)

## Inicando projeto em uma empresa

O que a empresa faz?
Quais sao os principais indicadores?
Como os executivos tomam suas decisões?
Baseado em que informações?

|
v

O que quero analisar? (que tipo de informação eu preciso? -> Indicador/Medida ou variavel)
Como quero analisar? (de que maneira eu quero ver essa informação? -> Dimensão)

Exemplo

Vendemos R$ 10000,00.

Vendemos R$ 10000,00 em Notebooks em Março.


## Matriz Dimenção X Indicador

Linhas - Indicador:
- Vendas
- Custos
- Lucro
- ...
  

Colunas - Dimensão:
- Cliente
- Empresa
- Tempo
- ...



|      |Cliente|Empresa|Tempo|
|---   |---    |---    |---  |
|Vendas| x     | x     |     |
|Custos|       |       |x    |
|Lucro |       | x     |     |

x -> cruzamento que faça sentido
nem sempre todos os indicadores vao cruzar com todas as dimensoes


exemplo:

- Posso ver Vendas por Cliente e por Produto
- Custo de Materia Prima, posso ver por Produto, e NÃO por cliente (regra varia por lógica de negócio)


|               |Cliente|Produto|
|---            |---    |---    |
|Vendas         | x     | x     |
|Custo Mat Prima|       | x     |


## Projetar Tabelas

Datawarehouse é um banco de dados, composto de tabelas, campos, registros, indices, chaves primarias e enstrangeiras
Unico diferencial é que o desenho do datawarehouse em suas caracteristicas sera a matriz de dimensão indicador.

As Tabelas são divididos em 2 grandes grupos:
- Tabelas de dimensão
- Tabelas de fato -> Grava uma ocorrencia, no momento tempo, quando algo ocorre com determinado indicador, é registrado aqui.


Como descobrir as tabelas de fato a partir da matriz de dimensao indicador?
Uma tabela de fato é o conjunto de dimensoes e indicadores que possuam os mesmo cruzamentos. Exemplo:

||Dim1|Dim2|Dim3|Dim4|
|---|---|---|---|---|
|Ind1|a|a|a|a|
|Ind2|a|a|a|a|
|Ind3||b|b|b|
|Ind4||b|b|b|
|Ind5|c|c|c||
|Ind6|c|c|c||



Fato A = Indicador1,2 e Dim1,2,3,4 
Fato B = Indicador3,4 e Dim2,3,4 
Fato C = Indicador5,6 e Dim1,2,3

Cada fato é uma tabela, e todas as Dimensoes devem ser uma Chave Primaria de outra tabela 


