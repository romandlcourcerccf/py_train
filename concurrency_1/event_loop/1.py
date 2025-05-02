import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 6000))
server_socket.listen()

def accept_connection(server_socket):


    while True:
        print('Before. accept')
        client_socker, address = server_socket.accept()
        print('Connect from ', address)

def send_message():
    while True:
        print('Before recv')
        request = client_socker.recv(4096)

        if not request:
            break
        else:
            responce = 'Hello world!\n'.encode()
            client_socker.send(responce)

    
    print('Outside inner loop')
    client_socker.close()
