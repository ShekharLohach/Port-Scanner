import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket connected")
except socket.error as err:
    print("connection failed")

port = 123
# try:
#     host_ip = socket.gethostbyname("www.google.com")
# except socket.gaierror:
#     print("there was a error")
#     sys.exit()
host_ip = "127.0.0.1"
s.bind(("", port))
s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()
    print('got a connection from',addr)
    c.send('tnx for connecting')
    c.close()
# s.connect((host_ip,port))
