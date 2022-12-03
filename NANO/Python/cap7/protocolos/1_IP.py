import socket

while True:
    url=input("Digite uma URL ")
    ip=socket.gethostbyname(url)
    print("O Ip referente a Url informada é",ip)
    if url=="":
        break