import socket
import pickle
import json
import marshal
from cryptography.fernet import Fernet


class ClientSide:
    def __init__(self, port, file_type=None, send_file=False, dictionary={}):
        self.dictionary = dictionary
        self.file_type = file_type
        self.send_file = send_file

        try:
            # Create a socket object and connect to the specified host and port
            self.s = socket.socket()
            self.host = socket.gethostname()
            self.port = port
            self.s.connect((self.host, self.port))

        except socket.error as err:
            # If an error occurs, print the error message
            print(f'Failed to connect to socket.{err}')

    def create_dict(self):
        # Clear the dictionary
        self.dictionary = {}

        # Input field for user to enter dictionary key(s) and value(s)
        key = input('Enter a key for the dictionary (press q to quit): ')

        # While loop to extend dictionary contents
        # User to press 'q' to close the dictionary
        while key != 'q':
            value = input('Enter a value for the key: ')
            self.dictionary[key] = value
            key = input('Enter another key for the dictionary (press q to quit): ')

    def serialised_binary(self):
        # Serialise the dictionary to binary
        self.dictionary = pickle.dumps(self.dictionary)
        
    def serialised_json(self): 
        # Serialise the dictionary to JSON
        self.dictionary = json.dumps(self.dictionary).encode()

    def serialised_xml(self):
        # Serialise the dictionary to XML
        self.dictionary = marshal.dumps(self.dictionary)

    def send_message(self):
        # If dictionary is empty, prompt user to enter dictionary values
        if len(self.dictionary) == 0:
            self.create_dict()

        # Serialise dictionary based on file type    
        if self.file_type == 'binary':
            self.serialised_binary()
        elif self.file_type == 'json':
            self.serialised_json()
        elif self.file_type == 'xml':
            self.serialised_xml()

        self.s.send(self.dictionary)

    def send_text_file(self):
        # Find a way to serialise text file and send through socket
        file_name = input('Enter text file location: ')
        encrypt = input('Would you like to encrypt? (y/n)')
       
        with open(file_name, 'rb') as f:
                file_contents = f.read()

        if encrypt == 'n':
            self.serialised_data = pickle.dumps(file_contents)

        else:
            # Generate a random key
            key = Fernet.generate_key()

            # Initialize the Fernet object with the key
            fernet = Fernet(key)

            self.serialised_data = pickle.dumps(fernet.encrypt(file_contents))

        self.s.send(self.serialised_data)

    def run_client(self):
        if self.send_file == True:
            self.send_text_file()
        else:
            self.send_message()


client = ClientSide(56789, send_file=True)
client.run_client()
