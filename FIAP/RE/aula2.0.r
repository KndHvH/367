> #uniao intersecção e diferenca de vetores
>
> vendedor1 <- c("Nike","Adidas","Olympikus")
> vendedor2 <- c("Adidas","Mizuno","Topper")
>
> union(vendedor1,vendedor2)
[1] "Nike"      "Adidas"    "Olympikus" "Mizuno"    "Topper"
> intersect(vendedor1,vendedor2)
[1] "Adidas"
> setdiff(vendedor2,vendedor1)
[1] "Mizuno" "Topper"
> setdiff(vendedor1,vendedor2)
[1] "Nike"      "Olympikus"
>
>
> arroz_marcas <- c("Camil","Tio João","Prato Fino")
> feijao_marcas <- c("Kicaldo","Milano","Urbano")
>
> interaction(arroz_marcas,feijao_marcas)
[1] Camil.Kicaldo     Tio João.Milano   Prato Fino.Urbano
9 Levels: Camil.Kicaldo Prato Fino.Kicaldo Tio João.Kicaldo ... Tio João.Urbano
>
> #outras formas de combinacoes
>
> a <- c("Camisa 1","Camisa 2")
> b <- c("Calca 1","Calca 2","Calca 3")
>
> expand.grid(a,b)
      Var1    Var2
1 Camisa 1 Calca 1
2 Camisa 2 Calca 1
3 Camisa 1 Calca 2
4 Camisa 2 Calca 2
5 Camisa 1 Calca 3
6 Camisa 2 Calca 3
>
> #vetores logicos
>
> produtos <-c("TV","REFRIGERADOR","NOTEBOOK","CELULAR")
> quantidades <-c(30,36,20,15)
>
> quantidades>10
[1] TRUE TRUE TRUE TRUE
>
> quantidades[3] == 60
[1] FALSE
> quantidades2 <- quantidades*2
>
> nomes <- c("Maria","Joao","Luiza","Paula")
>
> match("Paula",nomes)
[1] 4