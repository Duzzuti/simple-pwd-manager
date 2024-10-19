import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import hashes
import settings

from data import Data

# string used to verify password
correctBytes = "kolajlfdalöfdasnifjnasnofjasidfnoiasnfkajsfndjkasdfoasdjfioasdiujf\n".encode()

# Function to generate a key from a password
def generate_key(password: str, salt: bytes) -> bytes:
    kdf = Scrypt(
        length=32,
        salt=salt,
        backend=default_backend(),
        n=settings.n,
        r=settings.r,
        p=settings.p
    )
    return kdf.derive(password.encode())

# Function to decrypt data
def decrypt(data: bytes, key: bytes) -> bytes:
    iv = data[:16]  # The first 16 bytes are the IV
    encrypted_data = data[16:]  # The rest is the encrypted data
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    paddedData = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Remove padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(paddedData) + unpadder.finalize()
    return data

# Function to decrypt a file and returns the unpadded data or an empty byte string if some error occurs
def decrypt_file(inputFile: str, password: str) -> bytes:
    with open(inputFile, 'rb') as f:
        fileData = f.read()
    
    salt = fileData[:16]  # Extract the salt (first 16 bytes)
    encryptedData = fileData[16:]  # The rest is encrypted data

    key = generate_key(password, salt)
    try:
        decDataPadded = decrypt(encryptedData, key)
        if is_password_correct(decDataPadded):
            return decDataPadded[len(correctBytes):]
        else:
            return b""
    except:
        return b""

# Function to encrypt data
def encrypt(data: bytes, key: bytes) -> bytes:
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    paddedData = padder.update(data) + padder.finalize()
    encryptedData = encryptor.update(paddedData) + encryptor.finalize()
    return iv + encryptedData

# Function to encrypt a file
def encrypt_file(data: Data, outputFile: str, password: str):
    salt = os.urandom(16)  # Generate a random salt
    key = generate_key(password, salt)

    # add correct string at the start of the file
    fileData = correctBytes
    # add data

    fileData += data.byteData

    encryptedData = encrypt(fileData, key)
    
    with open(outputFile, 'wb') as f:
        f.write(salt + encryptedData)

def is_password_correct(encData: bytes) -> bool:
    return not(len(encData) < len(correctBytes) or encData[:len(correctBytes)] != correctBytes)