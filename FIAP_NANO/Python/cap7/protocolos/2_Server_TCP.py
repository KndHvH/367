from socket import *

server = "127.0.0.1" #localhost
port = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((server,port))
obj_socket.listen(2)

print("Aguardando cliente...")

while True:
    con, client = obj_socket.accept()
    print("Conectando com:",client)
    while True:
        recieved_msg = str(con.recv(1024))
        print("Recebemos: ", recieved_msg)
        send_msg = b"Ola Cliente"
        con.send(send_msg)
        break
    con.close()
