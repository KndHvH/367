'''arquivo = open("arquivo1.txt","w")

arquivo.write("Meu primeiro arquivo, ai que festa!")

arquivo.close()'''

x=1
while x==1:
    with open("arquivo1.txt","a") as arquivo:
        arquivo.write("\nHakuna Matata!!")