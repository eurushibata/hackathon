#!/usr/bin/env python
import socket
import json

''' Test connection and parser to json'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',8888))
result = json.loads(s.recv(1024))
for key in sorted(result.keys()):
    print key, result[key]
s.close()
