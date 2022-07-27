from socket import *

server = "127.0.0.1" #localhost
port = 43210
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((server,port))
print("Servidor pronto....")

while True:
    data, origem = obj_socket.recvfrom(65535)
    print("Origem....:",origem)
    print("Dados....:",data.decode())
    response = input("Digite a resposta")
    obj_socket.sendto(response.encode(),origem)

obj_socket.close()