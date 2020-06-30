#!/usr/bin/env python3

# Peter Thompson
# CSCI 373 - Cybersecurity
# Networking Lab - Task 1
# 2019-04-04

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(60) # 60 seconds
SERV = ('www.google.com',80)
req = b'GET / HTTP/1.0\r\n\r\n'

s.connect(SERV)
s.sendall(req)

response = b''
while True:
    recvd = s.recv(1024)
    if not recvd:
        break
    response += recvd

print('WE GOT:\n',response)
s.close()


#write to file, for fun
FILENAME = 'google.html'
try:
    open(FILENAME,'x')
except FileExistsError:
    os.remove(FILENAME)
    open(FILENAME,'x')
f = open(FILENAME,'wb')
f.write(response)
