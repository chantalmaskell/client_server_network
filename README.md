# Client-Server Network using Python

The code in this project consists of a client file and server file. To run the code, it is recommended to open these files in Visual Studio Code (VSC), and open two side-by-side terminals so each component of the client/server code can be understood with ease as they run.

## Table of Contents

- [Background](#background)
- [Dictionary Serialisation](#pickle)
- [Encryption](#encryption)
- [Install](#install)
- [Directory Tree](#directorytree)
- [License](#license)

## Background

To run this project, on the client file, locate 'client = ClientSide(56789, send_file=True)'. Here, please specify True if you are wanting to transfer a file. Alternatively, change this to False if you wish to send a serialised dictionary. When sending a text file, the client (user) has the option to encrypt the file using a 'y/n' prompt.

If sending a serialised dictionary, you will be guided through the steps to alter the file type for serialisation in the next section.

### Dictionary Serialisation 

When sending a dictionary from the client, the user has the ability to define which type of serialisation they want for the transfer: 'binary', 'json', or 'xml'. When the serialisation type is specified, the client code will match this input with the corresponding serialisation method. For example, 'binary' serialisation uses the *pickle* module. The server-side code reflects the inputted file type and uses the Magic module to deserialise the client dictionary.

By default, the user is able to input a dictionary from a prompt on the client-side code, where the user will be asked to enter a 'key' and then its corresponding 'value' pair. If you want to change this, please update the 'dictionary={}' value in the __init__ and replace this with the variable of your dictionary. This will bypass the manual dictionary input stage.

### Encryption

The client code has a prompt that will reveal if the user changes the default argument within the ClientSide initialisation to True. The prompt is a simple 'y/n' that enables the user to encrypt the text file prior to sending it to the server. If the user selects 'n', a standard serialised file will be sent to the server using pickle.dumps(). If the user does proceed to encrypt the file however, the fernet.encrypt() encryption method will be applied to the file before being serialised and sent to the server.

## Install

To run the code from the server and client files, please ensure you have the latest version of Python installed. For unit testing, run:
$ pytest unit_test.py

## Directory Tree

├── Client
<br>
│├── client.py
<br>
└── Server
<br>
├── server.py
<br>
├── requirements.txt
<br>
├── README.md
<br>
├── unittest.py
<br>
└── LICENSE

## License

[MIT © Chantal Maskell.](../LICENSE)
