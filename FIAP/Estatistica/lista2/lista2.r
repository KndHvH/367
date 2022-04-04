#1 - C

#2 - A

#3
sample(70:100,5)

#4 - E

#5

emprestimo <- matrix( c(NA, NA, NA), nrow = 4, ncol = 3, dimnames = list(NULL,c("Nome", "Salario", "Idade")))

emprestimo[1,] <- c("Marcos de Aguiar",4000,44)
emprestimo[2,] <- c("Paula Miranda",2500,56)
emprestimo[3,] <- c("Emilio Santos",1200,76)
emprestimo[4,] <- c("Pryscilla de Albuquerque",3400,40)

#6
emprestimo[2,2] <- c(5500.33)

#7
emprestimo[,2] <- round(as.numeric(emprestimo[,2]) * 0.7, digits=2)

#8
media_salario <- mean(as.numeric(emprestimo[,2]))

#9 -
colnames(emprestimo) <- c("Nome", "Salario", "Idade") ##??