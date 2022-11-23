with open ("pagina.html","w") as pag:
    pag.write("<body> <h1> Teste Pag WEB </h1>")
    pag.write("<br><h2> Abaixo alguns nomes do projeto: </h2>")
    pag.write("<h3>")
    nome=""

    while nome!="SAIR":
        nome = input("Digite o nome ou sair: ").upper()
        if nome!="SAIR":
            pag.write("<br>"+nome)
    pag.write("</h3></body>")