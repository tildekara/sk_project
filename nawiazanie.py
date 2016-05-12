# -*- coding: utf-8 -*-

import socket

HOST = '192.168.1.102'
PORT = 8863
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
for i in range(5):
	s.send("Czesc {}\n".format(i))
data = s.recv(1000)

print(data)
print("Reclieved {} bytes".format(len(data)))