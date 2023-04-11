O que analisar -> Vendas, Estoque, Status
Como analisar -> Tempo, Categoria, Local, Cliente, Loja, Produto

### Matriz Dimensao x Indicador

|       |Tempo|Categoria|Local|Cliente|Loja |Produto|
|---    |---  |---      |---  |---    |---  |---    |
|Vendas |  X  |  X      |  X  |   X   |  X  |  X    |
|Estoque|  X  |  X      |     |       |     |  X    | 
|Status |  X  |  X      |  X  |   X   |  X  |  X    |



### Fato A

|       |Tempo|Categoria|Local|Cliente|Loja |Produto|
|---    |---  |---      |---  |---    |---  |---    |
|Vendas |  X  |  X      |  X  |   X   |  X  |  X    |
|Status |  X  |  X      |  X  |   X   |  X  |  X    |


### Fato B

|       |Tempo|Categoria|Produto|
|---    |---  |---      |---    |
|Estoque|  X  |  X      |  X    | 



### Análise do relacionamento

|           | Categoria | Cidade | Estado | Cliente | Loja | Produto |
|-----------|-----------|--------|--------|---------|------|---------|
| Categoria | x         | x      | x      | x       | x    | x       |
| Cidade    | n:n       | x      | x      | x       | x    | x       |
| Estado    | n:n       | 1:n    | x      | x       | x    | x       |
| Cliente   | n:n       | 1:n    | 1:n    | x       | x    | x       |
| Loja      | n:n       | 1:n    | 1:n    | n:n     | x    | x       |
| Produto   | 1:n       | n:n    | n:n    | n:n     | n:n  | x       |