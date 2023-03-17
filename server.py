import socket
import pickle

# Define port number
port = 56789    

# Socket initialisation
s = socket.socket()
host = socket.gethostname() 

# Bind port and host
s.bind((host, port))

# Listen for connection from client
s.listen(5)
print('Server listening....')

while True:
    # Establish connection with client
    conn, addr = s.accept()
    print('Got connection from', addr)
    # data = conn.recv(4096)
    # print('Message received from client: ', repr(data))

    # Serialisation of dictionary from client
    dictionary_bytes = conn.recv(1024)
    dictionary = pickle.loads(dictionary_bytes)

    # Format key value pairs and delimet with colon
    for key, value in dictionary.items():
        print(key, ':', value)

    # Send message to client with UTF-8 encoding
    conn.send(('Dictionary received by server').encode('utf-8'))

    # Close connection with client
    conn.close()
    print('Connection with', addr, 'closed.')
    break

# End socket connection with client
s.close()
print('Server closed.')
conn.send(('Thank you for connecting. Connection will now end.').encode('utf-8'))