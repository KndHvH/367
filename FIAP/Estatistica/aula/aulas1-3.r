#SEQUENCIAS
#CriaÃ§Ã£o de sequencias - utilizada em criaÃ§Ã£o de funÃ§oe de base de dados

#CriaÃ§Ã£o com elementos
1:20
15:20
seq(1,25)
seq(1,25,2) #criaÃ§Ã£o se quÃªncia de 1 atÃ© 25, com passo 2
seq(1,25,0.5) #criaÃ§Ã£o se quÃªncia de 1 atÃ© 25, com passo 0.5

#CriaÃ§Ã£o com repetiÃ§Ãµes
rep(3,4) #repete o 3 4 vezes
rep(1:4,5) #repete  sequencia de 1 atÃ© 4, 5 vezes
produtos
rep(produtos,2) #repere a sequencia de profutos, 2 vezes
rep(produtos,3,each=2) #repete a sequencia de produtos 3 vezes, com 2 repetiÃ§Ãµes do objeto

#Sequencias usando amostras aleatÃ³rias
# com repetiÃ§Ã£o
sample(1:30,10) #retira 10 nÃºmeros aleatÃ³rios, entre 1 e 30 (sample = amostra)
sample(1:30,10,replace=T) #amostra com repetiÃ§Ã£o possÃ­vel

#sem repetiÃ§ao
sample(1:30,10,replace=F)

#Acessando elementos da sequÃªncia
doc_produtos<-100:150 #cria um vetor de 100 atÃ© 150
doc_produtos 
doc_produtos[3] #acessa o elemnto da posiÃ§Ã£o 3 
doc_produtos[3:9] #acessa o elemnto da posiÃ§Ã£o 3 atÃ© 9
doc_produtos[c(4,10)] #consulta das posiÃ§oes 4 e 10
doc_produtos[3]<-1002 #substitui o terceiro objeto do vetor por 1002
doc_produtos


# Matrizes - CriaÃ§Ã£o usando vetores
produtos  #criado nas aulas anteriores
quantidades #criado nas aulas anteriores
vendas<-cbind(produtos,quantidades) #cria matrizes por colunas
vendas
vendas<-rbind(produtos,quantidades) #cria matrizes por linhas
vendas

# Matrizes usando o matrix()
matrix(1:20, nrow =4 ,ncol=5) #matriz com elemtnos de 1 atÃ© 20, em 4 linhas e 5 colunas
matrix("Brasil", nrow =4 ,ncol=5) #matriz "Brasil" com 4 linhas e 5 colunas
matrix(0, nrow =4 ,ncol=5) #matriz nula de 4 linhas e 5 colunas

matrix(1:20, nrow =4 ,ncol=5,byrow = T) #cria a matriz por linha
matrix(1:30, nrow =4 ,ncol=5,byrow = T) #um erro possÃ­vel!
matrix(1:5, nrow =4 ,ncol=5,byrow = T) #cria uma matriz com elemntos de 1 a 5, com 4 linhas e 5 colunas
matrix(1:5, nrow =4 ,ncol=5,byrow = F) #cria matriz com sequencia por colunas
matrix(1:5, nrow =4 ,ncol=5) #cria matriz com sequencia por colunas



# ACESSANDO uma matriz criada
vendas
produtos[3]
vendas[1,2] #imprime o elemento da linha 1 e coluna 2
vendas[1,] #imprime a linha 1 toda
vendas[,2] #imprime a coluna 2 toda
vendas[2:4,] #imprime da linha 2 a 4, todas as colunas
vendas[2:4,1] #imprime da linha 2 a 4, apenas da coluna 1

vendas[4,2] #mostra o elemento da linha 4, coluna 2
vendas[2,1] #mostra o elemento 2 da coluna 1



# Modificando matrizes
vendas_Jan<-vendas
vendas_Fev<-vendas_Jan

vendas_Fev[,2]<- as.numeric(vendas_Jan[,2]) + 2

vendas_Fev[1,1]<-c("Televisor") #Mudando o nome TV para TELEVISOR
vendas_Fev[3,] <- c("PC",40) #Mudando o nome NOTEBOOK para PC
vendas_Fev[2:4,2] <- c(12,100,30) #Mudando elementos da linha 2 a 4, pelos elementos 12, 100, 30
vendas_Fev[c(1,4),1] <- c("TV","Smartphone") #Mudando o nome dos elementos 1 e 4 da coluna 1

vendas_Fev[,-1] #mostra todos as colunas, menos a coluna 1
vendas_Fev[-2,] #mostra todas as linhas, menos a linha 2
vendas_Fev[-1,-2] #mostra todo, menos a linha 1 e a coluna 2
vendas_Fev <- vendas_Fev[-4,] #exclui a linha 4
vendas_Fev


# OperaÃ§Ãµes com Matrizes
carlos<-c(120,130,400,230)
marcos<-c(20,334,420,130)
maria<-c(22,28,19,10)

vendas_Reais <- cbind(carlos,marcos,maria)
vendas_Reais

dim(vendas_Reais) #mostra as dimensÃµes da matriz
dim(vendas_Reais)[1] #nÃºmero de elementos de linhas
dim(vendas_Reais)[2] #nÃºmero de elementos de colunas
nrow(vendas_Reais) #nÃºmero de elementos de linhas
ncol(vendas_Reais) #nÃºmero de elementos de linhas

#dim()[2]  igual a  ncol()
# dim()[1]  igual a nrow()

vendas_Reais - 2
vendas_Reais <- vendas_Reais + 5 #Modifica o vetor venda, acrescentando 5 unidades

comissoes <- vendas_Reais*0.10 #cria o vetor COMISSOES com 10% das vendas
comissoes/2
comissoes ^ 2 
sqrt(comissoes)
log(comissoes)

comissoes
sum(comissoes[,1]) #soma todas as linhas da coluna 1
sum(comissoes[,2]) #soma todas as linhas da coluna 2
sum(comissoes[,3]) #soma todas as linhas da coluna 3
sum(comissoes) #soma de todas as comissÃµes

comissoes
mean(comissoes[,1]) #mÃ©dia de todas as linhas da coluna 1
mean(comissoes[,2]) #mÃ©dia de todas as linhas da coluna 2
mean(comissoes[,3]) #mÃ©dia de todas as linhas da coluna 3
mean(comissoes) #mÃ©dia de todas as comissÃµes

vendas_Reais
mean(vendas_Reais[,1]) #mÃ©dia de todas as linhas da coluna 1
mean(vendas_Reais[,2]) #mÃ©dia de todas as linhas da coluna 1
mean(vendas_Reais[,3]) #mÃ©dia de todas as linhas da coluna 1
mean(vendas_Reais) #mÃ©dia de todas as vendas
sum(vendas_Reais) #soma de todas as vendas


Jan<-comissoes*2 #guardando informaÃ§Ã£o no vetor comissÃµes de Janeiro
Fev<-comissoes #guardando informaÃ§Ã£o no vetor comissÃµes de Fevereiro

#OperaÃ§Ãµes com matrizes
Jan + Fev
Jan - Fev
Jan*Fev

dim(Jan)
dim(Fev)


# Curiosidades sobre Matrizes
A<-matrix(0,nrow = 5,ncol = 10) #Cria uma matriz nula com 5 linhas e 10 colunas
image(A)


A<-matrix(1:50,nrow = 5,ncol = 10)
image(A)
contour(A)
contour(volcano)
persp(A)
persp(volcano)


# Curiosidades em Matrizes (parte 2)
#2*X = 10
solve(2,10)

#3X + 2Y = 8
#1X + 1Y = 2
linha1<-c(3,2,8) #linha 1 do sistema linear
linha2<-c(1,1,2) #linha 2 do sistema linear
A<-rbind(linha1,linha2) #criaÃ§Ã£o do sistema linear
solve(A[,1:2],A[,3]) #resolve o sistema linear

det(A[,-3])  #determinante da matriz criada, eliminando a terceira coluna (matriz quadrada)
t(A) # matriz transposta (inverte as linhas com as colunas)


#ARRAYS
#CrianÃ§Ã£o usando Matrizes
#array(elementos, dimensoes, nomesdasdimensoes)

A<-matrix(1:20,4,5) #matriz com elementos de 1 a 20, 4 linhs e 5 colunas
A
array(A, dim = c(4,5,2)) #cria 2 matrizes de 4 linhas, 5 colunas  
array(A, dim = c(4,5)) #retirando a dimensÃ£o das quantidades de matrizes, ficamos apenas com uma matriz
array(0, dim = c(3,4,2)) #criando 2 matriz nulas, com 3 linhas e 4 colunas  
array(c("TV","Geladeira","Rack"),dim =c(3,2,3)) #Cria 3 matrizes com 3 linhas e 2 colunas


# CriaÃ§Ã£o de Arrays usando vetores   
vendas<-c(12,24,30)
produtos<-c("TV","Geladeira","Cama")

array(c(produtos,vendas),dim = c(3,2,2))
vendas_totais<-array(c(produtos,vendas),dim = c(3,2,3)) #3 matrizes, 3 linhas e 2 colunas


# Nomenando as dimensÃµes
nomes_variaveis<-c("Produtos","Quantidade") #nomes das colunas
nomes_matrizes<-c("Janeiro","Fevereiro","MarÃ§o") #nomes dos arrays
nomes_linhas<-c("Marcos","JoÃ£o","Maria") #nomes das linhas
array(c(produtos,vendas),dim = c(3,2,3),dimnames = list(nomes_linhas,nomes_variaveis,nomes_matrizes))
#array com 3 matrizes, 3 linhas e 2 colunas nomeadas


# Acessando os elementos do Array
vendas_totais <- array(c(produtos,vendas),dim = c(3,2,3),dimnames = list(nomes_linhas,nomes_variaveis,nomes_matrizes))
vendas_totais
dim(vendas_totais)

#vendas_totais[linha,coluna,matriz]
vendas_totais[,,1]  #vendas Janeiro
vendas_totais[,,2]  #vendas Fevereiro
vendas_totais[,,3]  #vendas MarÃ§o


vendas_totais[,1,]  # Coluna 1 de cada matriz = Produtos vendidos em cada mÃªs
vendas_totais[,2,]  # Coluna 2 de cada matriz = Quantidades vendidas em cada mÃªs

vendas_totais[1, ,]  # a Linha 1 de cada tabela = produÃ§Ã£o de Marcos (produtos e quantidades)
vendas_totais[2, ,]   # a Linha 2 de cada tabela = produÃ§Ã£o de JoÃ£o  (produtos e quantidades)
vendas_totais[3, ,]   # a Linha 3 de cada tabela = produÃ§Ã£o de Maria  (produtos e quantidades)


# CombinaÃ§Ã£o de DimensÃµes
vendas_totais[,2,1]  #vendas Janeiro, quantidades
vendas_totais[1,,1]  #produto e quantidade em janeiro (para Marcos)
vendas_totais[1,2,1]  #vendas em janeiro de Marcos

vendas_totais[3,2,3]  #vendas totais no mes de marÃ§o (para Maria)

vendas_totais[2,1,2] #produtos no mes de fevereiro (para JoÃ£o) 



#Modificando Arrays
# recapitulando a criaÃ§Ã£o de arrays usando vetores
vendas<-c(12,24,30)
produtos<-c("TV","Geladeira","Cama")

array(c(produtos,vendas),dim = c(3,2,2))
vendas_totais<-array(c(produtos,vendas),dim = c(3,2,3))

# Nomenando as dimensÃµes
nomes_variaveis<-c("Produtos","Quantidade")
nomes_matrizes<-c("Janeiro","Fevereiro","MarÃ§o")
nomes_linhas<-c("Marcos","JoÃ£o","Maria")
vendas_totais<-array(c(produtos,vendas),dim = c(3,2,3),dimnames = list(nomes_linhas,nomes_variaveis,nomes_matrizes))

#modificando elementos
vendas_totais[1,2,1]<-14
vendas_totais[2 ,, 2]<-c("Freezer",10)
vendas_totais[2:3,2,3]<-c(34,80) #Modificando uma sequencia
vendas_totais[c(1,3),2,3]<-c(20,40) #modificando elemento especÃ­fico


########## OperaÃ§Ãµes com Arrays



#Recapitulando a criaÃ§Ã£o de arrays usando vetores
vendas<-c(12,24,30)
produtos<-c("TV","Geladeira","Cama")

array(c(produtos,vendas),dim = c(3,2,2))
vendas_totais<-array(c(produtos,vendas),dim = c(3,2,3))

# Nomenando as dimensÃµes
nomes_variaveis<-c("Produtos","Quantidade")
nomes_matrizes<-c("Janeiro","Fevereiro","MarÃ§o")
nomes_linhas<-c("Marcos","JoÃ£o","Maria")
vendas_totais<-array(c(produtos,vendas),dim = c(3,2,3),dimnames = list(nomes_linhas,nomes_variaveis,nomes_matrizes))

vendas_totais[,2,]
sum(vendas_totais[,2,]) #apresenta erro
sum(as.numeric(vendas_totais[,2,])) #soma de unidades vendidas (soma das segundas colunas de cada matriz)
max(as.numeric(vendas_totais[,2,1]))
min(as.numeric(vendas_totais[,2,1]))



# OperaÃ§Ãµes com arrays - Dica extra
vendas_sem1<-c(12,10,8)
vendas_sem2<-vendas_sem1*2
vendas_sem3<-vendas_sem1*3
vendas_sem4<-vendas_sem3+15

array(c(vendas_sem1,vendas_sem2,vendas_sem3,vendas_sem4),dim=c(3,4,3))

nomes_variaveis<-c("Semana 1","Semana 2","Semana 3","Semana 4") #nome das colunas
nomes_linhas<-c("Marcos","JoÃ£o","Maria")
nomes_matrizes<-c("Janeiro","Fevereiro","MarÃ§o")

vendas_totais<-array(c(vendas_sem1,vendas_sem2,vendas_sem3,vendas_sem4),dim=c(3,4,3),
                     dimnames = list(nomes_linhas,nomes_variaveis,nomes_matrizes))


apply(vendas_totais, 2, sum) #Soma de todas as colunas  
apply(vendas_totais, 1, sum) #Soma de todas as linhas
apply(vendas_totais, 1, mean) #mÃ©dia por linha