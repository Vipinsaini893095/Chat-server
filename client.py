import socket
import multiprocessing
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 2222))
def send_messege():
    while True:
        text = input()
        s.send(str.encode(text, "utf-8"))


def recv_messege():
    while True:
        m = s.recv(1024)
        print(m.decode("utf-8"))


while True:
    recv_process = multiprocessing.Process(target=recv_messege)
    recv_process.start()
    send_messege()
