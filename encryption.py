import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.exceptions import InvalidSignature
import settings

def intToBytes(n: int, numBytes: int) -> bytes:
    try:
        return n.to_bytes(numBytes, byteorder="big", signed=False)
    except OverflowError:
        raise OverflowError("Some settings were set out of bounds.")

# Function to generate a key from a password
def generate_keys(password: str, salt: bytes, n = settings.n, r = settings.r, p = settings.p) -> tuple[bytes, bytes]:
    kdf = Scrypt(
        length=64,
        salt=salt,
        backend=default_backend(),
        n=2**n,
        r=r,
        p=p
    )
    keyBytes = kdf.derive(password.encode())
    return keyBytes[:32], keyBytes[32:]

# Function to decrypt data
def decrypt(data: bytes, key: bytes, hmacKey: bytes) -> bytes:
    if len(data) < 48:
        raise ValueError("Invalid data format. Not enough data for IV and HMAC value.")
    iv = data[:16]  # The first 16 bytes are the IV
    hmacValue = data[16:48]  # The next 32 bytes are the HMAC value
    encrypted_data = data[48:]  # The rest is the encrypted data

    # Verify HMAC
    hmac = HMAC(hmacKey, hashes.SHA256())
    hmac.update(iv + encrypted_data)
    try:
        hmac.verify(hmacValue)
    except InvalidSignature:
        raise InvalidSignature("HMAC verification failed. Incorrect password or tampered data.")
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    paddedData = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Remove padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(paddedData) + unpadder.finalize()
    return data

# Function to decrypt a file, returns empty bytes if the password is incorrect, throws an exception if the file is invalid formatted
def decrypt_file(inputFile: str, password: str) -> bytes:
    with open(inputFile, 'rb') as f:
        fileData = f.read()
    
    if len(fileData) == 0:
        raise ValueError("File is empty.")
    
    saltLen = fileData[0]  # The first byte is the length of the salt
    if saltLen > len(fileData) - 1:
        raise ValueError("Invalid file format: Salt length is greater than remaining file size.")
    salt = fileData[1:saltLen+1]  # Extract the salt
    if len(fileData) - saltLen - 1 < 3:
        raise ValueError("Invalid file format: Not enough data for n, r and p arguments.")
    readN = fileData[saltLen+1]
    readR = fileData[saltLen+2]
    readP = fileData[saltLen+3]

    encryptedData = fileData[saltLen+4:]  # The rest is encrypted data

    key, hmacKey = generate_keys(password, salt, readN, readR, readP)
    try:
        return decrypt(encryptedData, key, hmacKey)
    except InvalidSignature:
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
    salt = os.urandom(settings.saltLenBytes)  # Generate a random salt
    key, hmacKey = generate_keys(password, salt)

    encryptionData = encrypt(byteData, key, hmacKey)
    
    with open(outputFile, 'wb') as f:
        f.write(
            intToBytes(settings.saltLenBytes, 1) + 
            salt + 
            intToBytes(settings.n, 1) +
            intToBytes(settings.r, 1) +
            intToBytes(settings.p, 1) +
            encryptionData
        )