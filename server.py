import socket
import threading
import multiprocessing


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 2222))
s.listen(5)

#def send_commands(conn):
 #   recv_messege(conn)
  #  send_messege(conn)


def send_messege(conn):
    while True:
        text = input()
        conn.send(str.encode(text, "utf-8"))


def recv_messege(conn):
    while True:
        m = conn.recv(1024)
        print(m.decode("utf-8"))


msg = "connection successful"
while True:
    conn, address = s.accept()
    conn.send(str.encode(msg, "utf-8"))
    recv_process = multiprocessing.Process(target=recv_messege, args=(conn,))
    recv_process.start()
    send_messege(conn)
