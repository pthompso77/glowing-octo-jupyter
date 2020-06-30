#!/usr/bin/env python3

import socket
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])

# print('Trying to connect to {0}:{1}'.format(HOST,PORT))

#open socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
print('connected to',HOST)
while True:
    line = sys.stdin.readline()
    s.sendall(str.encode(line))
    response = s.recv(1024)
    print(response.decode())