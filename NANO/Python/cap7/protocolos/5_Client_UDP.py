from socket import *

server = "127.0.0.1" #localhost
port = 43210
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((server,port))
saida = ""

while saida != "X":
    msg = input("Sua Mensagem: ")
    obj_socket.sendto(msg.encode(),(server,port))
    data, origem = obj_socket.recvfrom(65535)
    print("Resposta servidor:",data.decode())
    saida = input("Digite x para sair! ").upper()

obj_socket.close()