> ###################################################################################
> #SEQUENCIAS
> #CriaÃ§Ã£o de sequencias - utilizada em criaÃ§Ã£o de funÃ§oe de base de dados
>
> #CriaÃ§Ã£o com elementos
> 1:20
 [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
> 15:20
[1] 15 16 17 18 19 20
> seq(1,25)
 [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
> seq(1,25,2) #criaÃ§Ã£o se quÃªncia de 1 atÃ© 25, com passo 2
 [1]  1  3  5  7  9 11 13 15 17 19 21 23 25
> seq(1,25,0.5) #criaÃ§Ã£o se quÃªncia de 1 atÃ© 25, com passo 0.5
 [1]  1.0  1.5  2.0  2.5  3.0  3.5  4.0  4.5  5.0  5.5  6.0  6.5  7.0  7.5  8.0  8.5  9.0
[18]  9.5 10.0 10.5 11.0 11.5 12.0 12.5 13.0 13.5 14.0 14.5 15.0 15.5 16.0 16.5 17.0 17.5
[35] 18.0 18.5 19.0 19.5 20.0 20.5 21.0 21.5 22.0 22.5 23.0 23.5 24.0 24.5 25.0
>
> #CriaÃ§Ã£o com repetiÃ§Ãµes
> rep(3,4) #repete o 3 4 vezes
[1] 3 3 3 3
> rep(1:4,5) #repete  sequencia de 1 atÃ© 4, 5 vezes
 [1] 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4
> produtos
[1] "TV"        "Geladeira" "Cama"
> rep(produtos,2) #repere a sequencia de profutos, 2 vezes
[1] "TV"        "Geladeira" "Cama"      "TV"        "Geladeira" "Cama"
> rep(produtos,3,each=2) #repete a sequencia de produtos 3 vezes, com 2 repetiÃ§Ãµes do objeto
 [1] "TV"        "TV"        "Geladeira" "Geladeira" "Cama"      "Cama"      "TV"
 [8] "TV"        "Geladeira" "Geladeira" "Cama"      "Cama"      "TV"        "TV"
[15] "Geladeira" "Geladeira" "Cama"      "Cama"
>
> #Sequencias usando amostras aleatÃ³rias
> # com repetiÃ§Ã£o
> sample(1:30,10) #retira 10 nÃºmeros aleatÃ³rios, entre 1 e 30 (sample = amostra)
 [1]  9  8 16 11 21  6 13 26 23 22
> sample(1:30,10,replace=T) #amostra com repetiÃ§Ã£o possÃ­vel
 [1]  1 29  1 15 26  1 12 18 22 21
>
> #sem repetiÃ§ao
> sample(1:30,10,replace=F)
 [1]  5 24 19 15 20 18 17  2 12 16
>
> #Acessando elementos da sequÃªncia
> doc_produtos<-100:150 #cria um vetor de 100 atÃ© 150
> doc_produtos
 [1] 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121
[23] 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143
[45] 144 145 146 147 148 149 150
> doc_produtos[3] #acessa o elemnto da posiÃ§Ã£o 3
[1] 102
> doc_produtos[3:9] #acessa o elemnto da posiÃ§Ã£o 3 atÃ© 9
[1] 102 103 104 105 106 107 108
> doc_produtos[c(4,10)] #consulta das posiÃ§oes 4 e 10
[1] 103 109
> doc_produtos[3]<-1002 #substitui o terceiro objeto do vetor por 1002
> doc_produtos
 [1]  100  101 1002  103  104  105  106  107  108  109  110  111  112  113  114  115  116
[18]  117  118  119  120  121  122  123  124  125  126  127  128  129  130  131  132  133
[35]  134  135  136  137  138  139  140  141  142  143  144  145  146  147  148  149  150
>
>
> # Matrizes - CriaÃ§Ã£o usando vetores
> produtos  #criado nas aulas anteriores
[1] "TV"        "Geladeira" "Cama"
> quantidades #criado nas aulas anteriores
[1] 30 36 20 15
> vendas<-cbind(produtos,quantidades) #cria matrizes por colunas
Warning message:
In cbind(produtos, quantidades) :
  number of rows of result is not a multiple of vector length (arg 1)
> vendas
     produtos    quantidades
[1,] "TV"        "30"
[2,] "Geladeira" "36"
[3,] "Cama"      "20"
[4,] "TV"        "15"
> vendas<-rbind(produtos,quantidades) #cria matrizes por linhas
Warning message:
In rbind(produtos, quantidades) :
  number of columns of result is not a multiple of vector length (arg 1)
> vendas
            [,1] [,2]        [,3]   [,4]
produtos    "TV" "Geladeira" "Cama" "TV"
quantidades "30" "36"        "20"   "15"
>
> # Matrizes usando o matrix()
> matrix(1:20, nrow =4 ,ncol=5) #matriz com elemtnos de 1 atÃ© 20, em 4 linhas e 5 colunas
     [,1] [,2] [,3] [,4] [,5]
[1,]    1    5    9   13   17
[2,]    2    6   10   14   18
[3,]    3    7   11   15   19
[4,]    4    8   12   16   20
> matrix("Brasil", nrow =4 ,ncol=5) #matriz "Brasil" com 4 linhas e 5 colunas
     [,1]     [,2]     [,3]     [,4]     [,5]
[1,] "Brasil" "Brasil" "Brasil" "Brasil" "Brasil"
[2,] "Brasil" "Brasil" "Brasil" "Brasil" "Brasil"
[3,] "Brasil" "Brasil" "Brasil" "Brasil" "Brasil"
[4,] "Brasil" "Brasil" "Brasil" "Brasil" "Brasil"
> matrix(0, nrow =4 ,ncol=5) #matriz nula de 4 linhas e 5 colunas
     [,1] [,2] [,3] [,4] [,5]
[1,]    0    0    0    0    0
[2,]    0    0    0    0    0
[3,]    0    0    0    0    0
[4,]    0    0    0    0    0
>
> matrix(1:20, nrow =4 ,ncol=5,byrow = T) #cria a matriz por linha
     [,1] [,2] [,3] [,4] [,5]
[1,]    1    2    3    4    5
[2,]    6    7    8    9   10
[3,]   11   12   13   14   15
[4,]   16   17   18   19   20
> matrix(1:30, nrow =4 ,ncol=5,byrow = T) #um erro possÃ­vel!
     [,1] [,2] [,3] [,4] [,5]
[1,]    1    2    3    4    5
[2,]    6    7    8    9   10
[3,]   11   12   13   14   15
[4,]   16   17   18   19   20
Warning message:
In matrix(1:30, nrow = 4, ncol = 5, byrow = T) :
  data length [30] is not a sub-multiple or multiple of the number of rows [4]
> matrix(1:5, nrow =4 ,ncol=5,byrow = T) #cria uma matriz com elemntos de 1 a 5, com 4 linhas e 5 colunas
     [,1] [,2] [,3] [,4] [,5]
[1,]    1    2    3    4    5
[2,]    1    2    3    4    5
[3,]    1    2    3    4    5
[4,]    1    2    3    4    5
> matrix(1:5, nrow =4 ,ncol=5,byrow = F) #cria matriz com sequencia por colunas
     [,1] [,2] [,3] [,4] [,5]
[1,]    1    5    4    3    2
[2,]    2    1    5    4    3
[3,]    3    2    1    5    4
[4,]    4    3    2    1    5
> matrix(1:5, nrow =4 ,ncol=5) #cria matriz com sequencia por colunas
     [,1] [,2] [,3] [,4] [,5]
[1,]    1    5    4    3    2
[2,]    2    1    5    4    3
[3,]    3    2    1    5    4
[4,]    4    3    2    1    5
>
>
>
> # ACESSANDO uma matriz criada
> vendas
            [,1] [,2]        [,3]   [,4]
produtos    "TV" "Geladeira" "Cama" "TV"
quantidades "30" "36"        "20"   "15"
> produtos[3]
[1] "Cama"
> vendas[1,2] #imprime o elemento da linha 1 e coluna 2
   produtos
"Geladeira"
> vendas[1,] #imprime a linha 1 toda
[1] "TV"        "Geladeira" "Cama"      "TV"
> vendas[,2] #imprime a coluna 2 toda
   produtos quantidades
"Geladeira"        "36"
> vendas[2:4,] #imprime da linha 2 a 4, todas as colunas
Error in vendas[2:4, ] : subscript out of bounds
> vendas[2:4,1] #imprime da linha 2 a 4, apenas da coluna 1
Error in vendas[2:4, 1] : subscript out of bounds
>
> vendas[4,2] #mostra o elemento da linha 4, coluna 2
Error in vendas[4, 2] : subscript out of bounds
> vendas[2,1] #mostra o elemento 2 da coluna 1
quantidades
       "30"
>
>
>
> # Modificando matrizes
> vendas_Jan<-vendas
> vendas_Fev<-vendas_Jan
>
> vendas_Fev[,2]<- as.numeric(vendas_Jan[,2]) + 2
Warning message:
NAs introduced by coercion
>
> vendas_Fev[1,1]<-c("Televisor") #Mudando o nome TV para TELEVISOR
> vendas_Fev[3,] <- c("PC",40) #Mudando o nome NOTEBOOK para PC
Error in `[<-`(`*tmp*`, 3, , value = c("PC", "40")) :
  subscript out of bounds
> vendas_Fev[2:4,2] <- c(12,100,30) #Mudando elementos da linha 2 a 4, pelos elementos 12, 100, 30
Error in `[<-`(`*tmp*`, 2:4, 2, value = c(12, 100, 30)) :
  subscript out of bounds
> vendas_Fev[c(1,4),1] <- c("TV","Smartphone") #Mudando o nome dos elementos 1 e 4 da coluna 1
Error in `[<-`(`*tmp*`, c(1, 4), 1, value = c("TV", "Smartphone")) :
  subscript out of bounds
>
> vendas_Fev[,-1] #mostra todos as colunas, menos a coluna 1
            [,1] [,2]   [,3]
produtos    NA   "Cama" "TV"
quantidades "38" "20"   "15"
> vendas_Fev[-2,] #mostra todas as linhas, menos a linha 2
[1] "Televisor" NA          "Cama"      "TV"
> vendas_Fev[-1,-2] #mostra todos , menos a linha 1 e a coluna
[1] "30" "20" "15"
> vendas_Fev <- vendas_Fev[-4,] #exclui a linha 4
> vendas_Fev
            [,1]        [,2] [,3]   [,4]
produtos    "Televisor" NA   "Cama" "TV"
quantidades "30"        "38" "20"   "15"
>
>
> # OperaÃ§Ãµes com Matrizes
> carlos<-c(120,130,400,230)
> marcos<-c(20,334,420,130)
> maria<-c(22,28,19,10)
>
> vendas_Reais <- cbind(carlos,marcos,maria)
> vendas_Reais
     carlos marcos maria
[1,]    120     20    22
[2,]    130    334    28
[3,]    400    420    19
[4,]    230    130    10
>
> dim(vendas_Reais) #mostra as dimensÃµes da matriz
[1] 4 3
> dim(vendas_Reais)[1] #nÃºmero de elementos de linhas
[1] 4
> dim(vendas_Reais)[2] #nÃºmero de elementos de colunas
[1] 3
> nrow(vendas_Reais) #nÃºmero de elementos de linhas
[1] 4
> ncol(vendas_Reais) #nÃºmero de elementos de linhas
[1] 3
>
> #dim()[2]  igual a  ncol()
> # dim()[1]  igual a nrow()
>
> vendas_Reais - 2
     carlos marcos maria
[1,]    118     18    20
[2,]    128    332    26
[3,]    398    418    17
[4,]    228    128     8
> vendas_Reais <- vendas_Reais + 5 #Modifica o vetor venda, acrescentando 5 unidades
>
> comissoes <- vendas_Reais*0.10 #cria o vetor COMISSOES com 10% das vendas
> comissoes/2
     carlos marcos maria
[1,]   6.25   1.25  1.35
[2,]   6.75  16.95  1.65
[3,]  20.25  21.25  1.20
[4,]  11.75   6.75  0.75
> comissoes ^ 2
      carlos  marcos maria
[1,]  156.25    6.25  7.29
[2,]  182.25 1149.21 10.89
[3,] 1640.25 1806.25  5.76
[4,]  552.25  182.25  2.25
> sqrt(comissoes)
       carlos   marcos    maria
[1,] 3.535534 1.581139 1.643168
[2,] 3.674235 5.822371 1.816590
[3,] 6.363961 6.519202 1.549193
[4,] 4.847680 3.674235 1.224745
> log(comissoes)
       carlos    marcos     maria
[1,] 2.525729 0.9162907 0.9932518
[2,] 2.602690 3.5234150 1.1939225
[3,] 3.701302 3.7495041 0.8754687
[4,] 3.157000 2.6026897 0.4054651
>
> comissoes
     carlos marcos maria
[1,]   12.5    2.5   2.7
[2,]   13.5   33.9   3.3
[3,]   40.5   42.5   2.4
[4,]   23.5   13.5   1.5
> sum(comissoes[,1]) #soma todas as linhas da coluna 1
[1] 90
> sum(comissoes[,2]) #soma todas as linhas da coluna 2
[1] 92.4
> sum(comissoes[,3]) #soma todas as linhas da coluna 3
[1] 9.9
> sum(comissoes) #soma de todas as comissÃµes
[1] 192.3
>
> comissoes
     carlos marcos maria
[1,]   12.5    2.5   2.7
[2,]   13.5   33.9   3.3
[3,]   40.5   42.5   2.4
[4,]   23.5   13.5   1.5
> mean(comissoes[,1]) #mÃ©dia de todas as linhas da coluna 1
[1] 22.5
> mean(comissoes[,2]) #mÃ©dia de todas as linhas da coluna 2
[1] 23.1
> mean(comissoes[,3]) #mÃ©dia de todas as linhas da coluna 3
[1] 2.475
> mean(comissoes) #mÃ©dia de todas as comissÃµes
[1] 16.025
>
> vendas_Reais
     carlos marcos maria
[1,]    125     25    27
[2,]    135    339    33
[3,]    405    425    24
[4,]    235    135    15
> mean(vendas_Reais[,1]) #mÃ©dia de todas as linhas da coluna 1
[1] 225
> mean(vendas_Reais[,2]) #mÃ©dia de todas as linhas da coluna 1
[1] 231
> mean(vendas_Reais[,3]) #mÃ©dia de todas as linhas da coluna 1
[1] 24.75
> mean(vendas_Reais) #mÃ©dia de todas as vendas
[1] 160.25
> sum(vendas_Reais) #soma de todas as vendas
[1] 1923
>
>
> Jan<-comissoes*2 #guardando informaÃ§Ã£o no vetor comissÃµes de Janeiro
> Fev<-comissoes #guardando informaÃ§Ã£o no vetor comissÃµes de Fevereiro
>
> #OperaÃ§Ãµes com matrizes
> Jan + Fev
     carlos marcos maria
[1,]   37.5    7.5   8.1
[2,]   40.5  101.7   9.9
[3,]  121.5  127.5   7.2
[4,]   70.5   40.5   4.5
> Jan - Fev
     carlos marcos maria
[1,]   12.5    2.5   2.7
[2,]   13.5   33.9   3.3
[3,]   40.5   42.5   2.4
[4,]   23.5   13.5   1.5
> Jan*Fev
     carlos  marcos maria
[1,]  312.5   12.50 14.58
[2,]  364.5 2298.42 21.78
[3,] 3280.5 3612.50 11.52
[4,] 1104.5  364.50  4.50
>
> dim(Jan)
[1] 4 3
> dim(Fev)
[1] 4 3
>
>
> # Curiosidades sobre Matrizes
> A<-matrix(0,nrow = 5,ncol = 10) #Cria uma matriz nula com 5 linhas e 10 colunas
> image(A)
Hit <Return> to see next plot:
>
> A<-matrix(1:50,nrow = 5,ncol = 10)
> image(A)
Hit <Return> to see next plot: contour(A)
> contour(volcano)
Hit <Return> to see next plot: persp(A)
> persp(volcano)
Hit <Return> to see next plot:
>
> # Curiosidades em Matrizes (parte 2)
> #2*X = 10
> solve(2,10)
[1] 5
>
> #3X + 2Y = 8
> #1X + 1Y = 2
> linha1<-c(3,2,8) #linha 1 do sistema linear
> linha2<-c(1,1,2) #linha 2 do sistema linear
> A<-rbind(linha1,linha2) #criaÃ§Ã£o do sistema linear
> solve(A[,1:2],A[,3]) #resolve o sistema linear
[1]  4 -2
>
> det(A[,-3])  #determinante da matriz criada, eliminando a terceira coluna (matriz quadrada)
[1] 1
> t(A) # matriz transposta (inverte as linhas com as colunas)
     linha1 linha2
[1,]      3      1
[2,]      2      1
[3,]      8      2
>
>
> #ARRAYS
> #CrianÃ§Ã£o usando Matrizes
> #array(elementos, dimensoes, nomesdasdimensoes)
>
> A<-matrix(1:20,4,5) #matriz com elementos de 1 a 20, 4 linhs e 5 colunas
> A
     [,1] [,2] [,3] [,4] [,5]
[1,]    1    5    9   13   17
[2,]    2    6   10   14   18
[3,]    3    7   11   15   19
[4,]    4    8   12   16   20
> array(A, dim = c(4,5,2)) #cria 2 matrizes de 4 linhas, 5 colunas
, , 1

     [,1] [,2] [,3] [,4] [,5]
[1,]    1    5    9   13   17
[2,]    2    6   10   14   18
[3,]    3    7   11   15   19
[4,]    4    8   12   16   20

, , 2

     [,1] [,2] [,3] [,4] [,5]
[1,]    1    5    9   13   17
[2,]    2    6   10   14   18
[3,]    3    7   11   15   19
[4,]    4    8   12   16   20

> array(A, dim = c(4,5)) #retirando a dimensÃ£o das quantidades de matrizes, ficamos apenas com uma matriz
     [,1] [,2] [,3] [,4] [,5]
[1,]    1    5    9   13   17
[2,]    2    6   10   14   18
[3,]    3    7   11   15   19
[4,]    4    8   12   16   20
> array(0, dim = c(3,4,2)) #criando 2 matriz nulas, com 3 linhas e 4 colunas
, , 1

     [,1] [,2] [,3] [,4]
[1,]    0    0    0    0
[2,]    0    0    0    0
[3,]    0    0    0    0

, , 2

     [,1] [,2] [,3] [,4]
[1,]    0    0    0    0
[2,]    0    0    0    0
[3,]    0    0    0    0

> array(c("TV","Geladeira","Rack"),dim =c(3,2,3)) #Cria 3 matrizes com 3 linhas e 2 colunas
, , 1

     [,1]        [,2]
[1,] "TV"        "TV"
[2,] "Geladeira" "Geladeira"
[3,] "Rack"      "Rack"

, , 2

     [,1]        [,2]
[1,] "TV"        "TV"
[2,] "Geladeira" "Geladeira"
[3,] "Rack"      "Rack"

, , 3

     [,1]        [,2]
[1,] "TV"        "TV"
[2,] "Geladeira" "Geladeira"
[3,] "Rack"      "Rack"

>
>
> # CriaÃ§Ã£o de Arrays usando vetores
> vendas<-c(12,24,30)
> produtos<-c("TV","Geladeira","Cama")
>
> array(c(produtos,vendas),dim = c(3,2,2))
, , 1

     [,1]        [,2]
[1,] "TV"        "12"
[2,] "Geladeira" "24"
[3,] "Cama"      "30"

, , 2

     [,1]        [,2]
[1,] "TV"        "12"
[2,] "Geladeira" "24"
[3,] "Cama"      "30"

> vendas_totais<-array(c(produtos,vendas),dim = c(3,2,3)) #3 matrizes, 3 linhas e 2 colunas
>
>
> # Nomenando as dimensÃµes
> nomes_variaveis<-c("Produtos","Quantidade") #nomes das colunas
> nomes_matrizes<-c("Janeiro","Fevereiro","MarÃ§o") #nomes dos arrays
> nomes_linhas<-c("Marcos","JoÃ£o","Maria") #nomes das linhas
> array(c(produtos,vendas),dim = c(3,2,3),dimnames = list(nomes_linhas,nomes_variaveis,nomes_matrizes))
, , Janeiro

       Produtos    Quantidade
Marcos "TV"        "12"
JoÃ£o  "Geladeira" "24"
Maria  "Cama"      "30"

, , Fevereiro

       Produtos    Quantidade
Marcos "TV"        "12"
JoÃ£o  "Geladeira" "24"
Maria  "Cama"      "30"

, , MarÃ§o

       Produtos    Quantidade
Marcos "TV"        "12"
JoÃ£o  "Geladeira" "24"
Maria  "Cama"      "30"

> #array com 3 matrizes, 3 linhas e 2 colunas nomeadas
>
>
> # Acessando os elementos do Array
> vendas_totais <- array(c(produtos,vendas),dim = c(3,2,3),dimnames = list(nomes_linhas,nomes_variaveis,nomes_matrizes))
> vendas_totais
, , Janeiro

       Produtos    Quantidade
Marcos "TV"        "12"
JoÃ£o  "Geladeira" "24"
Maria  "Cama"      "30"

, , Fevereiro

       Produtos    Quantidade
Marcos "TV"        "12"
JoÃ£o  "Geladeira" "24"
Maria  "Cama"      "30"

, , MarÃ§o

       Produtos    Quantidade
Marcos "TV"        "12"
JoÃ£o  "Geladeira" "24"
Maria  "Cama"      "30"

> dim(vendas_totais)
[1] 3 2 3
>
> #vendas_totais[linha,coluna,matriz]
> vendas_totais[,,1]  #vendas Janeiro
       Produtos    Quantidade
Marcos "TV"        "12"
JoÃ£o  "Geladeira" "24"
Maria  "Cama"      "30"
> vendas_totais[,,2]  #vendas Fevereiro
       Produtos    Quantidade
Marcos "TV"        "12"
JoÃ£o  "Geladeira" "24"
Maria  "Cama"      "30"
> vendas_totais[,,3]  #vendas MarÃ§o
       Produtos    Quantidade
Marcos "TV"        "12"
JoÃ£o  "Geladeira" "24"
Maria  "Cama"      "30"
>
>
> vendas_totais[,1,]  # Coluna 1 de cada matriz = Produtos vendidos em cada mÃªs
       Janeiro     Fevereiro   MarÃ§o
Marcos "TV"        "TV"        "TV"
JoÃ£o  "Geladeira" "Geladeira" "Geladeira"
Maria  "Cama"      "Cama"      "Cama"
> vendas_totais[,2,]  # Coluna 2 de cada matriz = Quantidades vendidas em cada mÃªs
       Janeiro Fevereiro MarÃ§o
Marcos "12"    "12"      "12"
JoÃ£o  "24"    "24"      "24"
Maria  "30"    "30"      "30"
>
> vendas_totais[1, ,]  # a Linha 1 de cada tabela = produÃ§Ã£o de Marcos (produtos e quantidades)
           Janeiro Fevereiro MarÃ§o
Produtos   "TV"    "TV"      "TV"
Quantidade "12"    "12"      "12"
> vendas_totais[2, ,]   # a Linha 2 de cada tabela = produÃ§Ã£o de JoÃ£o  (produtos e quantidades)
           Janeiro     Fevereiro   MarÃ§o
Produtos   "Geladeira" "Geladeira" "Geladeira"
Quantidade "24"        "24"        "24"
> vendas_totais[3, ,]   # a Linha 3 de cada tabela = produÃ§Ã£o de Maria  (produtos e quantidades)
           Janeiro Fevereiro MarÃ§o
Produtos   "Cama"  "Cama"    "Cama"
Quantidade "30"    "30"      "30"
>
>
> # CombinaÃ§Ã£o de DimensÃµes
> vendas_totais[,2,1]  #vendas Janeiro, quantidades
Marcos  JoÃ£o  Maria
  "12"   "24"   "30"
> vendas_totais[1,,1]  #produto e quantidade em janeiro (para Marcos)
  Produtos Quantidade
      "TV"       "12"
> vendas_totais[1,2,1]  #vendas em janeiro de Marcos
[1] "12"
>
> vendas_totais[3,2,3]  #vendas totais no mes de marÃ§o (para Maria)
[1] "30"
>
> vendas_totais[2,1,2] #produtos no mes de fevereiro (para JoÃ£o)
[1] "Geladeira"
>
>
>
> #Modificando Arrays
> # recapitulando a criaÃ§Ã£o de arrays usando vetores
> vendas<-c(12,24,30)
> produtos<-c("TV","Geladeira","Cama")
>
> array(c(produtos,vendas),dim = c(3,2,2))
, , 1

     [,1]        [,2]
[1,] "TV"        "12"
[2,] "Geladeira" "24"
[3,] "Cama"      "30"

, , 2

     [,1]        [,2]
[1,] "TV"        "12"
[2,] "Geladeira" "24"
[3,] "Cama"      "30"

> vendas_totais<-array(c(produtos,vendas),dim = c(3,2,3))
>
> # Nomenando as dimensÃµes
> nomes_variaveis<-c("Produtos","Quantidade")
> nomes_matrizes<-c("Janeiro","Fevereiro","MarÃ§o")
> nomes_linhas<-c("Marcos","JoÃ£o","Maria")
> vendas_totais<-array(c(produtos,vendas),dim = c(3,2,3),dimnames = list(nomes_linhas,nomes_variaveis,nomes_matrizes))
>
> #modificando elementos
> vendas_totais[1,2,1]<-14
> vendas_totais[2 ,, 2]<-c("Freezer",10)
> vendas_totais[2:3,2,3]<-c(34,80) #Modificando uma sequencia
> vendas_totais[c(1,3),2,3]<-c(20,40) #modificando elemento especÃ­fico
>
>
> ########## OperaÃ§Ãµes com Arrays
>
>
>
> #Recapitulando a criaÃ§Ã£o de arrays usando vetores
> vendas<-c(12,24,30)
> produtos<-c("TV","Geladeira","Cama")
>
> array(c(produtos,vendas),dim = c(3,2,2))
, , 1

     [,1]        [,2]
[1,] "TV"        "12"
[2,] "Geladeira" "24"
[3,] "Cama"      "30"

, , 2

     [,1]        [,2]
[1,] "TV"        "12"
[2,] "Geladeira" "24"
[3,] "Cama"      "30"

> vendas_totais<-array(c(produtos,vendas),dim = c(3,2,3))
>
> # Nomenando as dimensÃµes
> nomes_variaveis<-c("Produtos","Quantidade")
> nomes_matrizes<-c("Janeiro","Fevereiro","MarÃ§o")
> nomes_linhas<-c("Marcos","JoÃ£o","Maria")
> vendas_totais<-array(c(produtos,vendas),dim = c(3,2,3),dimnames = list(nomes_linhas,nomes_variaveis,nomes_matrizes))
>
> vendas_totais[,2,]
       Janeiro Fevereiro MarÃ§o
Marcos "12"    "12"      "12"
JoÃ£o  "24"    "24"      "24"
Maria  "30"    "30"      "30"
> sum(vendas_totais[,2,]) #apresenta erro
Error in sum(vendas_totais[, 2, ]) :
  invalid 'type' (character) of argument
> sum(as.numeric(vendas_totais[,2,])) #soma de unidades vendidas (soma das segundas colunas de cada matriz)
[1] 198
> max(as.numeric(vendas_totais[,2,1]))
[1] 30
> min(as.numeric(vendas_totais[,2,1]))
[1] 12
>
>
>
> # OperaÃ§Ãµes com arrays - Dica extra
> vendas_sem1<-c(12,10,8)
> vendas_sem2<-vendas_sem1*2
> vendas_sem3<-vendas_sem1*3
> vendas_sem4<-vendas_sem3+15
>
> array(c(vendas_sem1,vendas_sem2,vendas_sem3,vendas_sem4),dim=c(3,4,3))
, , 1

     [,1] [,2] [,3] [,4]
[1,]   12   24   36   51
[2,]   10   20   30   45
[3,]    8   16   24   39

, , 2

     [,1] [,2] [,3] [,4]
[1,]   12   24   36   51
[2,]   10   20   30   45
[3,]    8   16   24   39

, , 3

     [,1] [,2] [,3] [,4]
[1,]   12   24   36   51
[2,]   10   20   30   45
[3,]    8   16   24   39

>
> nomes_variaveis<-c("Semana 1","Semana 2","Semana 3","Semana 4") #nome das colunas
> nomes_linhas<-c("Marcos","JoÃ£o","Maria")
> nomes_matrizes<-c("Janeiro","Fevereiro","MarÃ§o")
>
> vendas_totais<-array(c(vendas_sem1,vendas_sem2,vendas_sem3,vendas_sem4),dim=c(3,4,3),
+                      dimnames = list(nomes_linhas,nomes_variaveis,nomes_matrizes))
>
>
> apply(vendas_totais, 2, sum) #Soma de todas as colunas
Semana 1 Semana 2 Semana 3 Semana 4
      90      180      270      405
> apply(vendas_totais, 1, sum) #Soma de todas as linhas
Marcos  JoÃ£o  Maria
   369    315    261
> apply(vendas_totais, 1, mean) #mÃ©dia por linha
Marcos  JoÃ£o  Maria
 30.75  26.25  21.75
