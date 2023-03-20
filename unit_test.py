import json
import pickle
import marshal
from cryptography.fernet import Fernet

def test_json():
    input_data = 'this is a test'

    serialised_json = json.dumps(input_data).encode()
    deserialised_json = json.loads(serialised_json)

    assert input_data==deserialised_json

def test_pickle():
    input_data = 'this is a test'

    serialised_json = pickle.dumps(input_data)
    deserialised_json = pickle.loads(serialised_json)

    assert input_data==deserialised_json

def test_xml():
    input_data = 'this is a test'

    serialised_json = marshal.dumps(input_data)
    deserialised_json = marshal.loads(serialised_json)

    assert input_data==deserialised_json

def test_encryption_file():
    message = b"This is a test"
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted = f.encrypt(message)

    with open('encryption.txt', 'wb') as f:
        pickle.dump(encrypted, f)

    with open('encryption.txt', 'rb') as f:
        output_data = pickle.load(f)

    assert encrypted == output_data

def test_file_save_test():
    input_data = 'this is a test'

    with open('text.txt', 'w') as f:
        f.write(input_data)

    with open('text.txt', 'r') as f:
        output_data = f.read()

    assert input_data==output_data
