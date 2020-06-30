#!/usr/bin/env python3

import sys
import socket

m = b'GET /index.html HTTP/1.0\r\n\r\n'
m= 'index.html'
def http_parse(msg):
    if (len(msg) < 3):
        PAGE = '/'
    else:
        PAGE = msg
    return PAGE
    
#http_parse(m)

#########

# HTTP Request

if(len(sys.argv)>2):
    PAGE = http_parse(sys.argv[2])
else:
    PAGE = '/'

print('let us fetch',PAGE)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(60)
SERV = (sys.argv[1],80)
reqHeader = 'GET {0} HTTP/1.0\r\n\r\n'.format(PAGE)

s.connect(SERV)
s.sendall(str.encode(reqHeader))

response = b''
while True:
    recv = s.recv(1024)
    if not recv:
        break
    response += recv
    
print(response.decode('utf-8','ignore'))
s.close()