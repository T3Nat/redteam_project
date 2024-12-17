import sys
import socket
import os

BUFFER = 4096

if __name__ == '__main__':

 port = <port>
 host = '<host>'
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect((host,port))
 
 file_name = "test.txt"
 print("------------------")
 file_size = os.path.getsize(file_name)
 s.send(str(file_size).encode('utf-8'))
 
 with open(file_name, 'rb') as fs:
       data = fs.read(BUFFER)
       while data:
             s.send(data)
             data = fs.read(BUFFER)
