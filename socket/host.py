import socket
import datetime

HOST = '0.0.0.0'
PORT = 3434

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    print("client {0} connected!".format(str(addr)))
    dt = datetime.datetime.now()
    message = "SEND" + str(dt)
    conn.send(b"message")
    print("sent: ", message)
    conn.close()