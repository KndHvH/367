> #1
> nomes <- c ("Marcos de Aguiar","Paula Miranda","Emilio Santos","Priscila de Albuquerque")
>
> #2
> nomes[4] <- c("Prycilla de Albuquerque")
>
> #3
> salario <- c(4000,2500,1200,3400)
>
> #4
> salario <- salario*0.70
>
> #5 - d
>
> #6 - b
>
> #7 - c
>
> #8 - a
> prova1 <- c(8,9,5,6,7,8,8,8,5)
>
> prova1[prova1 > 7]
[1] 8 9 8 8 8
>
>
> prova2 <- c(2,3,4,3,6,4,2,9,5)
>
> prova2[prova2==7]
numeric(0)
>
>
> prova3 <- c(1,6,2,9,1,10,2,9,2)
>
> length(prova2[prova2!=4])
[1] 7
>
> #9 F V F F
>
> prova1 <- c(3,6,4,2,7,8,5,6)
> prova2 <- c(6,10,3,6,4,2,7,5)
> prova3 <- c(10,10,5,7,4,6,2,7)
>
> sum (prova1, prova2, prova3)
[1] 135
>
> 100* ((prova2-prova1)/prova1)
[1] 100.00000  66.66667 -25.00000 200.00000 -42.85714 -75.00000  40.00000 -16.66667
>
> sum(prova1)/length(prova1)
[1] 5.125
>
> length(prova1[prova1<prova2])
[1] 4
>
> a = prova1<prova2
>
> a
[1]  TRUE  TRUE FALSE  TRUE FALSE FALSE  TRUE FALSE