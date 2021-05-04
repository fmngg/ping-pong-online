import socket
import pickle
from _thread import *
from player import Player

screen_width = 1280
screen_height = 720

server = "localhost"    # server ipv4
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as message:
    print(message)

s.listen(2)
print("Waiting for connection, server is running")

players = [Player(20, screen_height / 2 - 63, 10, 126, (70, 130, 180)),
           Player(screen_width - 30, screen_height / 2 - 63, 10, 126, (200, 200, 200))]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))

    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))

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
