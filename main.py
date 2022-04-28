import socket
import pickle

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 1234))
server_socket.listen()

def encode(packet):
    data = b""
    data += packet
    values = pickle.loads(data)
    return values

def send():

    data = b""
    while True:
        connection, client_addr = server_socket.accept()
        print('jetzt hamma eine connection, und zwar von', client_addr)
        while True:

            packet = connection.recv(200)
            daten=encode(packet)

            return(daten)
