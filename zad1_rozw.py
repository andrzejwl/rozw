import socket
import json

HOST = "172.104.229.108"
PORT = 5003

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    info = json.dumps({"username": "myname"})
    s.sendall(str.encode(info))
    data = s.recv(1024)

    msg = data.decode()
    print('Server reply:', msg)

    json_data = json.loads(msg)
    print("My session id:", json_data["session_id"])


    msg = json.dumps({"request": "ALL_ROOMS"})
    s.sendall(str.encode(msg))
    response = s.recv(1024).decode()
    print(response)

    msg = json.dumps({"request": "CREATE_ROOM", "data": "room1"})
    s.sendall(str.encode(msg))
    response = s.recv(1024).decode()
    print(response)

    s.close()
