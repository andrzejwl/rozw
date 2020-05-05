import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 50000      

print('Client 2 started!')

s.connect((host, port))        

while True:
    print("Your message:")
    msg = input()
    data = s.sendall(str.encode(msg))
    resp = s.recv(1024)
    print("Client 1:", resp.decode())

