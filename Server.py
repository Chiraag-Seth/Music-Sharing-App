import socket
from  threading import Thread
import time
import os

IP_ADDRESS = "127.0.0.1"
port = 8080
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def acceptConnections():
    global SERVER
    global clients
    while True:
        client, addr = SERVER.accept()
        print(client,addr)

def setup():
    print("IP Messenger")
    global port
    global IP_ADDRESS
    global SERVER
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, port))
    SERVER.listen(100)
    print("Server is waiting for incoming connections")
    acceptConnections()
setup_thread = Thread(target = setup)
setup_thread.start()

