import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.exceptions import InvalidSignature
from sys import exit
import traceback
import easygui

import settings

# Function to convert an integer to bytes in a standardized way
def intToBytes(n: int, numBytes: int) -> bytes:
    try:
        return n.to_bytes(numBytes, byteorder="big", signed=False)
    except OverflowError:
        raise OverflowError("Some settings were set out of bounds.")

# Function to generate two keys from a password
def generate_keys(password: str, salt: bytes, n = settings.n, r = settings.r, p = settings.p) -> tuple[bytes, bytes]:
    try:
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
    except Exception:
        print("Error while generating keys, probably due to invalid settings or corrupted data.")
        traceback.print_exc()
        exit()

# Function to decrypt a file, returns empty bytes if the password is incorrect, throws an exception if the file is invalid formatted
def decrypt_file(inputFile: str, password: str) -> bytes:
    with open(inputFile, 'rb') as f:
        fileData = f.read()
    
    if len(fileData) == 0:
        raise ValueError("File is empty.")
    
    # Extract version, salt, n, r and p
    majorVersion = fileData[0]
    minorVersion = fileData[1]
    version = "v" + str(majorVersion) + "." + str(minorVersion)
    if not settings.isFileCompatible(majorVersion, minorVersion):
        easygui.msgbox("The file was created with a newer version of the program. Please update the program to open the file. (File version: " + version + ", Program version: " + settings.version + ")", "Password Manager")
        exit()
    
    saltLen = fileData[2]
    if saltLen > len(fileData) - 1:
        raise ValueError("Invalid file format: Salt length is greater than remaining file size.")
    salt = fileData[3:saltLen+3]  # Extract the salt
    if len(fileData) - saltLen - 3 < 3:
        raise ValueError("Invalid file format: Not enough data for n, r and p arguments.")
    readN = fileData[saltLen+3]
    readR = fileData[saltLen+4]
    readP = fileData[saltLen+5]
    print("n: " + str(readN) + ", r: " + str(readR) + ", p: " + str(readP))

    # Extract iv, hmacValue and encryptedData
    iv = fileData[saltLen+6:saltLen+22]
    hmacValue = fileData[saltLen+22:saltLen+54]
    encryptedData = fileData[saltLen+54:]

    key, hmacKey = generate_keys(password, salt, readN, readR, readP)

    try:
        # Verify HMAC
        hmac = HMAC(hmacKey, hashes.SHA256())
        # update on all data except the hmacValue
        hmac.update(fileData[:saltLen+22] + fileData[saltLen+54:])
        try:
            hmac.verify(hmacValue)
        except InvalidSignature:
            return b""
        
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        paddedData = decryptor.update(encryptedData) + decryptor.finalize()
        
        # Remove padding
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        return unpadder.update(paddedData) + unpadder.finalize()

    except Exception:
        print("Error while decrypting file: ")
        traceback.print_exc()
        exit()

# Function to encrypt a file
def encrypt_file(byteData: bytes, outputFile: str, password: str):
    salt = os.urandom(settings.saltLenBytes)  # Generate a random salt
    key, hmacKey = generate_keys(password, salt)

    majorVersion = intToBytes(int(settings.version[1:].split(".")[0]), 1)  # Remove the "v" at the beginning
    minorVersion = intToBytes(int(settings.version.split(".")[1]), 1)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    paddedData = padder.update(byteData) + padder.finalize()
    encryptedData = encryptor.update(paddedData) + encryptor.finalize()

    writeDataFirstPart = majorVersion + \
                        minorVersion + \
                        intToBytes(settings.saltLenBytes, 1) + \
                        salt + \
                        intToBytes(settings.n, 1) + \
                        intToBytes(settings.r, 1) + \
                        intToBytes(settings.p, 1) + \
                        iv
    # Generate HMAC
    hmac = HMAC(hmacKey, hashes.SHA256(), backend=default_backend())
    hmac.update(writeDataFirstPart + encryptedData)
    hmacValue = hmac.finalize()
    
    with open(outputFile, 'wb') as f:
        f.write(
            writeDataFirstPart +
            hmacValue +
            encryptedData
        )