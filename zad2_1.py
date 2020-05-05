import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 50000      

print('Client 1 started!')
print('Waiting for connection...')

s.bind((host, port))        

s.listen(1)
#while True:
conn, addr = s.accept()

while True: 
    data = conn.recv(1024)
    print("Client 2:", data.decode())
    print("Your message:")
    msg = input()
    conn.sendall(str.encode(msg))


