













produtos <- matrix(NA, nrow = 7, ncol = 2, dimnames = list(NULL, c('Produto','Valor')))
produtos [,1] <- c('celular','teve','tablet','echo dot','caixa de som','relogio digital','fones')

produtos [,2] <- c(1200,3000,500,300,200,1000,300)

vendas <- matrix(NA, nrow = 1000, ncol = 3, dimnames = list(NULL, c('Produto','Quantidade','Mes')))
vendas[,2] <- sample(10:1000,1000, replace = TRUE)

vendas[,3] <- sample(1:12,1000, replace = TRUE)

vendas[,1] <- sample(produtos[,1],1000, replace = TRUE)


library(dplyr)
as.data.frame(vendas) %>% group_by(venda.)