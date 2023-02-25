import socketserver
import os

BUFFER_SIZE = 1024

# https://docs.python.org/3/library/socketserver.html

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip().decode()
        # print("{} wrote:".format(self.client_address[0])
        if self.data:
            if self.data.split()[0] == 'download':
                print('masuk download')
                # mencoba cari file
                try:
                    # print(f'files/{self.data.split()[1]}')
                    f = open(f'files/{self.data.split()[1]}','r')
                    # file ada
                    if f:
                        print('tes')
                        # variabel untuk header
                        file_name = self.data.split()[1]
                        file_path = f'files/{self.data.split()[1]}'
                        file_size = int(os.path.getsize(file_path))

                        header = f'file-name: {file_name},\\n\nfile-size: {file_size},\\n\n\\n\\n'
                        
                        self.request.send(f"{header}".encode())
                        with open(file_path, "rb") as f:
                            while True:
                                # read the bytes from the file
                                bytes_read = f.read(BUFFER_SIZE)
                                if not bytes_read:
                                    # file transmitting is done
                                    break
                                # we use sendall to assure transimission in 
                                # busy networks
                                self.request.sendall(bytes_read)
                # file tidak ketemu
                except OSError as e:
                    print('mohon maaf file tidak ada')
            else:
                print('Mohon maaf perintah tidak ditemukan')

        # just send back the same self.data, but upper-cased
        # self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
