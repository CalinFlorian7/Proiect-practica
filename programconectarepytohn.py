import socket
import json
HOST = '127.0.0.1'  # replace with the IP address of your computer running the C# program
PORT = 12345           # choose any free port number
import time
import threading
# open a socket and listen for incoming connections
temperatura_inregistrata=24.44
temp=str(temperatura_inregistrata)
status='-----'
import random

def afiseaza(status):
    while True:
        print(status)
        time.sleep(5)
# def receive_data(conn):
#     received_data = conn.recv(1024).decode()
#     print('Received:', received_data)
#     
# #     afiseaza_thread = threading.Thread(target=afiseaza, args=(status,))
# #     afiseaza_thread.start()
#     conn.close()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('test')
    # accept a client connection and send data
    while True:
       
        conn, addr = s.accept()
        print('Connected by', addr)
#         data = b'This is a message from MicroPython\n'
        data = temp.encode()
        conn.sendall(data)
        
#         receive_thread = threading.Thread(target=receive_data, args=(conn,))
#         receive_thread.start()
       
        conn.close()
        
        
        