# Import socket module
import socket

# Import pickle module for serialisation
import pickle

# Socket initialisation
s = socket.socket()
host = socket.gethostname()
port = 56789

# Connect host and port with server
s.connect((host, port))
# s.send(("Hello server").encode('utf-8'))

# Empty dictionary for client to populate
dictionary = {}

# Input field for user to enter dictionary key(s) and value(s)
key = input('Enter a key for the dictionary (press q to quit): ')

# While loop to extend dictionary contents
# User to press 'q' to close the dictionary
while key != 'q':
    value = input('Enter a value for the key: ')
    dictionary[key] = value
    key = input('Enter another key for the dictionary (press q to quit): ')

# Serialisation of dictionary object
dictionary_bytes = pickle.dumps(dictionary)
s.send(dictionary_bytes)

response = s.recv(1024).decode('utf-8')
print(response)

# End connection with server
s.close()
print('Connection ended with server.')