import socket
import threading
import time

def recv():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 8888))
    data = s.recv(1024).decode("utf-8")
    t = data.replace("[", '')
    t = t.replace("]", '')
    data= t.replace(" ",'')
    data = t.split(",")
    finger = data[1::2]
    # print(finger)
    return  finger




