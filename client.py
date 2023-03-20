import socket
import pickle
import json
import marshal
from cryptography.fernet import Fernet

# Client class
class ClientSide:
    # Initialising core variables
    def __init__(self, port, file_type=None, send_file=False, dictionary={}):
        self.dictionary = dictionary
        self.file_type = file_type
        self.send_file = send_file

        try:
            # Create socket object and connect to specified port on the server
            self.s = socket.socket()
            self.host = socket.gethostname()
            self.port = port
            self.s.connect((self.host, self.port))

        except socket.error as err:
            print(f'Failed to connect to socket.{err}')

    # Function to manually create dictionary
    def create_dict(self):
        self.dictionary = {}

        # Input field for user to enter dictionary key(s) and value(s)
        key = input('Enter a key for the dictionary (press q to quit): ')

        # While loop to extend dictionary contents
        # User to press 'q' to close the dictionary and send to the server
        while key != 'q':
            value = input('Enter a value for the key: ')
            self.dictionary[key] = value
            key = input('Enter another key for the dictionary (press q to quit): ')

    # Serialise dictionary to binary format
    def serialised_binary(self):
        self.dictionary = pickle.dumps(self.dictionary)
        
    # Serialise dictionary to JSON format
    def serialised_json(self):      
        self.dictionary = json.dumps(self.dictionary).encode()

    # Serialise dictionary to XML format
    def serialised_xml(self):
        self.dictionary = marshal.dumps(self.dictionary)

    # Send serialised dictionary to server
    def send_message(self):
        if len(self.dictionary) == 0:
            self.create_dict()

        if self.file_type == 'binary':
            self.serialised_binary()
        elif self.file_type == 'json':
            self.serialised_json()
        elif self.file_type == 'xml':
            self.serialised_xml()

        self.s.send(self.dictionary)

    # Function to send text file to server
    def send_text_file(self):
        # Prompt user to enter file location
        # Prompt user to add encryption to the file
        file_name = input('Enter text file location: ')
        encrypt = input('Would you like to encrypt? (y/n)')
       
        with open(file_name, 'rb') as f:
                file_contents = f.read()

        if encrypt == 'n':
            self.serialised_data = pickle.dumps(file_contents)

        else:
            # Generate a random key and encrypt the file contents
            key = Fernet.generate_key()

            # Initialize the Fernet object with the key
            fernet = Fernet(key)

            # Send the serialised data to the server
            self.serialised_data = pickle.dumps(fernet.encrypt(file_contents))

        self.s.send(self.serialised_data)

    # Function to run the overall client
    # and send either a dictionary or text file to server
    def run_client(self):
        if self.send_file == True:
            self.send_text_file()
        else:
            self.send_message()

# Create a client object with port and the option to send a file
client = ClientSide(56789, send_file=True)

# Run the client
client.run_client()
