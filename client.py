# -*- coding: utf-8 -*-

import socket

HOST = '192.168.0.10'
PORT = 9998
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
for i in range(5):
    s.send(b"Czesc {}\n")
data = s.recv(1000)

print(data)
print("Reclieved {} bytes".format(len(data)))