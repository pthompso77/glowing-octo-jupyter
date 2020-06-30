#!/usr/bin/env python3

# Peter Thompson
# CSCI 373 - Cybersecurity
# Networking Lab - Task 2
# 2019-04-09

import socket
import datetime
import os

PORT = 8080
HOST = '127.0.0.1'
CONN = (HOST,PORT)


def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        while True:
            try:
                s.bind(CONN)
                break
            except:
                PORT += 1
        s.listen()
        print('server up and listening to {0}'.format(CONN))
        
        while True:
            print('waiting')
            conn,addr = s.accept()
            print('got connection from {0}'.format(addr))
            
            with conn:
                process_http(conn)
            
            print('done with connection from {0}'.format(addr))
        s.close()
            
            
def process_http(conn):
    buff = ''
    while True:
        data = conn.recv(1024)
        if not data:
            break
        buff += data.decode('utf-8','ignore')
        
        if buff.endswith('\r\n\r\n'):
            break
    
    print('request:')
    print(buff)
    response = parse_request(buff)
    if not response:
        response = respond_404('')
    print(response)
    conn.sendall(str.encode(response))
    
def parse_request(req):
    if not req.startswith('GET'):
        return False
    (method,uri,rest) = req.split(' ',2)
    
    if uri.endswith('/'):
        uri += 'index.html'
    filepath = os.getcwd()+uri
    print('looking for {0}'.format(uri))
    if os.path.isfile(filepath):
        with open(filepath) as fd:
            return make_header('200 OK',fd.read())
    else:
        print('Not found')
        return False
    
    
def respond_404(url):
    html = '''<!DOCTYPE HTML>
    <HTML>
    <HEAD>
    <TITLE>
    40404040 NOT FOUNDDDD
    </TITLE>
    </HEAD>
    <BODY>
    <H1>
    40404040404 NOT FOUND
    </H1>
    <img src='https://user-images.githubusercontent.com/24848110/33519396-7e56363c-d79d-11e7-969b-09782f5ccbab.png'>
    <p>The requested page was not found</p>
    </BODY>
    </HTML>
    '''
    return make_header("404 Not Found", html)

def make_header(code, load):
    header = 'HTTP/1.0 {0}\r\n'.format(code)
    header += 'Date: {0}\r\n'.format(datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT'))
    header += 'Server: my_serverrr\r\n'
    header += 'Content Length: {0}\r\n'.format(len(load))
    header += 'Connection: close\r\n'
    header += 'Content-type: text/html\r\n'
    header += '\r\n' #last line
    return header + load



if __name__=='__main__':
    main()