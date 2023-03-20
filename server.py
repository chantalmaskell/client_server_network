import socket
import pickle
import json
import marshal
import magic

# Server class
class ServerSide:
    # Initialising core variables
    def __init__(self, port, save_file=False, print_result=True):
        self.s = socket.socket()
        self.host = socket.gethostname()
        self.port = port
        self.print_result = print_result

    def server_check(self):
        # Binding the socket to the host and port
        self.s.bind((self.host, self.port))

        # Listen for incoming connections
        try:
            self.s.listen(5)
            print('Server is listening...')
        # Raise exception if connection is not received
        except:
            raise Exception('Server failed!')

    def test_connection(self):
        while True:
            try:
                # Accept incoming connections from client
                self.conn, addr = self.s.accept()
                if addr is None:
                    raise Exception('Problem with address.')
                else:
                    print('Got connection from', addr)
                    break
            except:
                raise Exception('Connection error.')

    def deserialise_dict(self):
        # Receive data from the client
        received_dict = self.conn.recv(4096)

        # Use magic to determine the file type of the received data
        m = magic.Magic(mime=True)
        file_type = m.from_buffer(received_dict)
        # file_saved = False

        # Check if the contents of the dictionary match the format of binary data
        if file_type == 'application/octet-stream':
            try:
                # Depickling binary data
                self.loaded_dict = pickle.loads(received_dict)
                print('Binary file type received. Now depickling...')
                
                # Checks if recieved dict is bytes object
                if isinstance(self.loaded_dict, bytes):
                    # file_saved = True
                    with open("C:\\Users\chana\\Documents\\GitHub\\client_server_network\\server_cache\\text.txt", 'wb') as f:
                        # Saving received bytes object as text file
                        f.write(self.loaded_dict)

                    print('Text File Saved.')
                    # else:
                    #     print(self.loaded_dict)
            except:
                print('XML file type received. Now loading.')
                self.loaded_dict = marshal.loads(received_dict)

        # Check if the contents of the dictionary match the format of JSON data
        elif file_type == 'text/plain':
        # Check if the contents of the dictionary match the format of JSON data
            try:
                self.loaded_dict = json.loads(received_dict.decode('utf-8'))
                print('JSON file type received. Now Loading')
            except:
                raise Exception('Invalid JSON file.')
            
        else:
            # Unsupported file type received
            print(f'File type: {file_type} not supported')

        if self.print_result == True:
            print(self.loaded_dict)

    def run_server(self):
        self.server_check()
        self.test_connection()
        self.deserialise_dict()

server = ServerSide(56789)
server.run_server()