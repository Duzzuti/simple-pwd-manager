import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.exceptions import InvalidSignature
import settings

# Function to generate a key from a password
def generate_keys(password: str, salt: bytes) -> tuple[bytes, bytes]:
    kdf = Scrypt(
        length=64,
        salt=salt,
        backend=default_backend(),
        n=settings.n,
        r=settings.r,
        p=settings.p
    )
    keyBytes = kdf.derive(password.encode())
    return keyBytes[:32], keyBytes[32:]

# Function to decrypt data
def decrypt(data: bytes, key: bytes, hmacKey: bytes) -> bytes:
    iv = data[:16]  # The first 16 bytes are the IV
    hmacValue = data[16:48]  # The next 32 bytes are the HMAC value
    encrypted_data = data[48:]  # The rest is the encrypted data

    # Verify HMAC
    hmac = HMAC(hmacKey, hashes.SHA256())
    hmac.update(iv + encrypted_data)
    try:
        hmac.verify(hmacValue)
    except InvalidSignature:
        raise ValueError("HMAC verification failed. Incorrect password or tampered data.")
    
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

    key, hmacKey = generate_keys(password, salt)
    try:
        return decrypt(encryptedData, key, hmacKey)
    except ValueError:
        return b""
    except Exception as e:
        print(e)
        exit()

# Function to encrypt data
def encrypt(data: bytes, key: bytes, hmacKey: bytes) -> bytes:
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    paddedData = padder.update(data) + padder.finalize()
    encryptedData = encryptor.update(paddedData) + encryptor.finalize()
    
    # Generate HMAC
    hmac = HMAC(hmacKey, hashes.SHA256(), backend=default_backend())
    hmac.update(iv + encryptedData)
    hmacValue = hmac.finalize()
    
    return iv + hmacValue + encryptedData

# Function to encrypt a file
def encrypt_file(byteData: bytes, outputFile: str, password: str):
    salt = os.urandom(16)  # Generate a random salt
    key, hmacKey = generate_keys(password, salt)

    encryptedData = encrypt(byteData, key, hmacKey)
    
    with open(outputFile, 'wb') as f:
        f.write(salt + encryptedData)