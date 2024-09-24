import os
import easygui

import encryption
from data import Data

userDataDir = "userData"
defaultEncFileWithoutExt = "pEnc"

def init():
    if not os.path.isdir(userDataDir):
        os.mkdir(userDataDir)
    userDataValid = checkUserDataValidity()
    if not userDataValid[0]:
        easygui.msgbox("The userData directory contains files or directories that should not be there (namely: "+ userDataValid[1] +"). Please remove them.", "Password Manager")
        exit()

def saveLastUsedFile(file):
    with open("lastUsedFile.txt", "w") as f:
        f.write(file)

def getLastUsedFile() -> str:
    if not os.path.isfile("lastUsedFile.txt"):
        return None
    with open("lastUsedFile.txt", "r") as f:
        return f.read()

def verifyFileName(fileName) -> bool:
    validChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    if not fileName:
        easygui.msgbox("The file name cannot be empty.", "Password Manager")
        return False
    for char in fileName:
        if char not in validChars:
            easygui.msgbox("The file name contains invalid characters ('"+char+"'). Only letters, numbers and underscores are allowed.", "Password Manager")
            return False
    return True

def isUserDataDirEmpty() -> bool:
    return len(os.listdir(userDataDir)) == 0

def createEncryptedFile(fileName, password):
    open(os.path.join(userDataDir, fileName + ".enc"), 'wb').close()
    saveLastUsedFile(fileName)
    encryption.encrypt_pdata(Data(), os.path.join(userDataDir, fileName + ".enc"), password)

#check if only .enc files are in the userData directory
def checkUserDataValidity() -> tuple[bool, str]:
    for object in os.listdir(userDataDir):
        if not os.path.isfile(os.path.join(userDataDir, object)) or not object.endswith(".enc"):
            return (False, object)
    return (True, None)


def getAllFilesInDir(directory) -> list:
    files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            files.append(file)
    return files