import socket
from _thread import *

screen_width = 1280
screen_height = 720

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as message:
    print(message)

s.listen(2)
print("Waiting for connection, server is running")


def read_pos(str):
    str = str.split(",")
    return int(str[0]),  int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos = [(10, screen_height / 2 - 63), (screen_width - 20, screen_height / 2 - 63)]


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = "localhost"
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending: ", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
