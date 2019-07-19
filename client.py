import socket

s = socket.socket()
def pscan(port):
    try:

        host_ip = '127.0.0.1'
        s.connect((host_ip,port))
        return True
    except:
        return False

for x in range(25):
    if pscan(x):
        print(x, " is open")
    else:
        print(x ,"is closed")