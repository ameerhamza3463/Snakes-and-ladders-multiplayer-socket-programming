import socket
from _thread import *
import sys

server = socket.gethostbyname(socket.gethostname())
# server = "0.0.0.0"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

pos = [(406-25,606-25),(406-25,606-25)]
playerturn = 0
connected_players = 0

def read_data(str):
    t = str.split(";")
    p = t[1].split(":")
    player_id = p[0]
    player_data = p[1].split(",")
    return int(t[0]), int(player_id), int(player_data[0]), int(player_data[1])


def make_data(tup, player, turn, connected_players):
    return str(connected_players) + "/" + str(turn) + ";" + str(player) + ":" + str(tup[0]) + "," + str(tup[1])
    

def threaded_client(conn, player):
    global playerturn
    global connected_players
    turn = player
    conn.send(str.encode(make_data(pos[player], player, turn, connected_players)))
    reply = ""
    
    while True:
        try:
            data = read_data(conn.recv(2048).decode())
            tempturn = data[0]
            pos[player] = (data[2], data[3])

            if tempturn == -1:
                playerturn = playerturn
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
            else:
                if not data:
                    print("Disconnected")
                    break
                else:
                    if player == 1:
                        reply = pos[0]
                        playerturn = tempturn
                    else:
                        reply = pos[1]
                        playerturn = tempturn
                    print("Received: ", data)
                    print("Sending : ", reply)

            conn.sendall(str.encode(make_data(reply, player, playerturn, connected_players)))
        except:
            break

    print("Lost connection")
    if connected_players > 0:
        connected_players -= 1
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    connected_players = currentPlayer
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
        