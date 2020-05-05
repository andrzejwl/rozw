import socket
import json

HOST = "172.104.229.108"
PORT = 9001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    info = json.dumps({"username": myname})
    s.sendall(str.encode(info))
    data = s.recv(2048)

    msg = data.decode()
    print('Server reply:', msg)


    try:
        json_data = json.loads(msg)

        if json_data["session_id"]:
            print("session open")
            mysession = json_data["session_id"]
        else:
            print("[ERR] session not open")
            exit(1)


    except Exception as e:
        print(e)
        print(msg)
        print("[ERR] Error parsing server reply")
        exit(1)


    print("[INFO] sending data to server")


    msg = json.dumps({"request": "ALL_ROOMS"})
    s.sendall(str.encode(msg))
    response = s.recv(2048).decode()
    print(response)

    msg = json.dumps({"request": "CREATE_ROOM", "data": {"name": "room1", "size": 5}})
    s.sendall(str.encode(msg))
    response = s.recv(2048).decode()
    print(response)

    s.close()