import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

from data import Data

# string used to verify password
correct_bytes = "kolajlfdalöfdasnifjnasnofjasidfnoiasnfkajsfndjkasdfoasdjfioasdiujf\n".encode()

# Function to generate a key from a password
def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=5000000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Function to decrypt data
def decrypt(data: bytes, key: bytes) -> bytes:
    iv = data[:16]  # The first 16 bytes are the IV
    encrypted_data = data[16:]  # The rest is the encrypted data
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Remove padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data

# Function to decrypt a file
def decrypt_file(input_file: str, password: str):
    with open(input_file, 'rb') as f:
        file_data = f.read()
    
    salt = file_data[:16]  # Extract the salt (first 16 bytes)
    encrypted_data = file_data[16:]  # The rest is encrypted data

    key = generate_key(password, salt)
    try:
        return decrypt(encrypted_data, key)
    except:
        return ""

# Function to encrypt data
def encrypt(data: bytes, key: bytes) -> bytes:
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return iv + encrypted_data

# Function to encrypt a file
def encrypt_pdata(data: Data, output_file: str, password: str):
    salt = os.urandom(16)  # Generate a random salt
    key = generate_key(password, salt)

    # add correct string at the start of the file
    file_data = correct_bytes
    # add data

    file_data += data.getByteData()

    encrypted_data = encrypt(file_data, key)
    
    with open(output_file, 'wb') as f:
        f.write(salt + encrypted_data)