import socket
import select
import sys

server_address = ('127.0.0.1', 5002)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

input_socket = [server_socket]

try:
    while True:
        read_ready, write_ready, exception = select.select(input_socket, [], [])
        
        for sock in read_ready:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                input_socket.append(client_socket)        
            
            else:            	
                data = sock.recv(1024)
                
                if data:
                    sock.send(data)
                    # data: teks string
                    data = data.decode()

                    if data.split()[0] == 'download':
                        print('masuk download')

                        try:
                            print(f'files/{data.split()[1]}')
                            f = open(f'files/{data.split()[1]}','r')
                            if f:
                                print('hellow')
                        except OSError as e:
                            print('mohon maaf file tidak ada')
                    else:
                        print('Mohon maaf perintah tidak ditemukan')
                else:                    
                    sock.close()
                    input_socket.remove(sock)
except KeyboardInterrupt:        
    server_socket.close()
    sys.exit(0)
