> log(1)
[1] 0
> factorial(5)
[1] 120
> abs(-100)
[1] 100
> sin(30)
[1] -0.9880316
> sin(pi/6)
[1]  0.5

x<-c(3,4,5)
#    1 2 3

vendas <- c(12,15,3,5)
meses <- c("Jan","Fev","Mar","Abr")

vendas2 <- scan()
#  input

> vendas[1]
[1] 12

> vendas[c(1,4)]
[1] 12  5

> vendas[c(1:3)]
[1] 12 15  3

> vendas[3] <- 13
> vendas
[1] 12 15 13  5

vendas[c(1,4)] <-c(0,90)
vendas