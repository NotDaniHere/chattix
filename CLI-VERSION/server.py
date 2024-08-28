import threading
import socket

host = '127.0.0.1' #localhost
port = 40132

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []
server_password = "RELLSFTW"


credentials_db = {"Dani": "VatraDunarii2016", "PLACEHOLDER_NICKNAME": "CLEAR"}

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} has left the chat.'.encode('ascii'))
            nicknames.remove(nickname)
            break


def receive(sv_password):
    while True:
        client, address = server.accept()
        nickname = "PH_NN"
        password = "clear"
        client.send('LOGIN'.encode('ascii'))
        credentials = client.recv(1024).decode('ascii')
        for i, j in enumerate(credentials):
            if j == "/":
                if credentials[i+1] == "P":
                    if credentials[i+2] == "A":
                        if credentials[i+3] == "S":
                            if credentials[i+4] == "S":
                                if credentials[i+5] == "W":
                                    if credentials[i+6] == "D":
                                        if credentials[i+7] == "_":
                                            if credentials[i+8] == "S":
                                                if credentials[i+9] == "E":
                                                    if credentials[i+10] == "P":
                                                        if credentials[i+11] == '/':
                                                            username = credentials[0:i]
                                                            credentials_no_user = credentials[i+12:-1]
                                                            print(credentials_no_user)
                                                            for i, j in enumerate(credentials_no_user):
                                                                if credentials_no_user[i] == "/":
                                                                    if credentials_no_user[i+1] == "S":
                                                                        if credentials_no_user[i+2] == "E":
                                                                            if credentials_no_user[i+3] == "R":
                                                                                if credentials_no_user[i+4] == "V":
                                                                                    if credentials_no_user[i+5] == "E":
                                                                                        if credentials_no_user[i+6] == "R":
                                                                                            if credentials_no_user[i+7] == "_":
                                                                                                if credentials_no_user[i+8] == "S":
                                                                                                    if credentials_no_user[i+9] == "E":
                                                                                                        if credentials_no_user[i+10] == "P":
                                                                                                            if credentials_no_user[i+11] == '/':
                                                                                                                user_password = credentials_no_user[0:i]
                                                                                                                server_password = credentials_no_user[i+12:]
                                                                                                                if not server_password == sv_password:
                                                                                                                    client.close()
                                                            
        if username in credentials_db:
            if credentials_db[username] == user_password:
                print(f"Connected with {str(address)}.")
                nicknames.append(username)
                clients.append(client)

                print(f'{username} has logged on the server.')
                broadcast(f'{username} has joined the chat'.encode('ascii'))
                client.send('Connected to the server.'.encode('ascii'))

                thread = threading.Thread(target = handle, args = (client,))
                thread.start()
            else:
                client.send('LOGIN_ERROR'.encode('ascii'))
        else:
            client.send('LOGIN_ERROR'.encode('ascii'))


receive(server_password)

