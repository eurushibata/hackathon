#!/usr/bin/env python

import socket
import sys
from thread import *
import json

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error code: ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'


s.listen(10)
print 'Socket now listening'

# Function for handling connections. This will be used to create threads
def clientthread(conn):
    # Sending message to connected client
    while True:
        try:
            data = {'message':'hello world!','test':123.4}
            conn.send(json.dumps(data))
            conn.close()
        except:
            conn.close()



# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call
    conn , addr = s.accept()
    # display client information
    print 'Connected with ' + addr[0] +':' + str(addr[1])
    # start new thread takes 1st argument as a function name to be run , second is the tuple of arguments to the function.
    start_new_thread(clientthread , (conn,))
s.close()
