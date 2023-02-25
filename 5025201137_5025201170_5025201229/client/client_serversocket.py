import socket
import sys

HOST, PORT = "localhost", 9999
BUFFER_SIZE = 1024

def parsing_header(header):
    info = header.split(',\\n')
    file_name = info[0].split()
    file_name = file_name[1]
    file_size = info[1]
    file_size = file_size[1:].split()
    file_size = file_size[1]
    print(file_name) 
    print(file_size)

    return file_name, file_size

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))

    message = sys.stdin.readline()
    sock.send(bytes(message, "utf-8"))

    received_data = sock.recv(BUFFER_SIZE).decode('utf-8')
    print(received_data)
    file_name, file_size = parsing_header(received_data)

    print(file_name)
    with open(file_name, 'wb+') as f:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = sock.recv(BUFFER_SIZE)
            if not bytes_read:    
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
