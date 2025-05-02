import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()

connections = []


try:

    while True:

        connection, client_address = server_socket.accept()
        print(f'Got connection from {client_address}')
        connections.append(connection)

        buffer = b''
        while buffer[-2:] != '\r\n':
            data = connection.recv(2)
            if not data:
                break
            else:
                print(f'I got data {data}!')
                buffer += data
    
        print(f'All data is {buffer}')
        connection.sendall(buffer)

finally:
    server_socket.close()

