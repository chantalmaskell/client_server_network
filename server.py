import socket
import pickle
import json
import marshal
import magic

class ServerSide:
    def __init__(self, port, save_file=False):
        self.s = socket.socket()
        self.host = socket.gethostname()
        self.port = port

    def server_check(self):
        self.s.bind((self.host, self.port))

        try:
            self.s.listen(5)
            print('Server is listening...')
        except:
            raise Exception('Server failed!')

    def test_connection(self):
        while True:
            try:
                self.conn, addr = self.s.accept()
                if addr is None:
                    raise Exception('Problem with address.')
                else:
                    print('Got connection from', addr)
                    break
            except:
                raise Exception('Connection error.')

    def deserialise_dict(self):
        received_dict = self.conn.recv(4096)
        m = magic.Magic(mime=True)
        file_type = m.from_buffer(received_dict)
        file_saved = False

        if file_type == 'application/octet-stream':
        # Check if the contents of the dictionary match the format of binary data
            try:
                self.loaded_dict = pickle.loads(received_dict)
                print('Binary file type received. Now depickling.')
                
                # Checks if recieved dict is bytes object
                if isinstance(self.loaded_dict, bytes):
                    file_saved = True
                    with open("C:\\Users\chana\\Documents\\GitHub\\client_server_network\\server_cache\\text.txt", 'wb') as f:
                        f.write(self.loaded_dict)

                    print('Text File Saved.')
            except:
                print('XML file type received. Now loading.')
                self.loaded_dict = marshal.loads(received_dict)

        elif file_type == 'text/plain':
        # Check if the contents of the dictionary match the format of JSON data
            try:
                self.loaded_dict = json.loads(received_dict.decode('utf-8'))
                print('JSON file type received. Now Loading')
            except:
                raise Exception('Invalid JSON file.')
            
        else:
            print(f'File type: {file_type} not supported')

        if file_saved == False:
            print(self.loaded_dict)

    def run_server(self):
        self.server_check()
        self.test_connection()
        self.deserialise_dict()

server = ServerSide(56789)
server.run_server()