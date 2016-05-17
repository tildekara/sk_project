# -*- coding: utf-8 -*-

import socket

HOST = '10.68.16.72' #tutaj podaje swoj ip, jesli chce, zeby ze mna sie polaczylo
PORT = 8874
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((HOST,PORT)) 
#s.bind((HOST, PORT)) #Uwaga -- te nawiasy są ważne, określaja pythonową krotkę (touple)
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while 1:
    data = conn.recv(1000).decode()
    if not data: break
    conn.sendall(data)
    print (data)
conn.close()