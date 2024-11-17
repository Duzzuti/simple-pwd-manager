import os
import easygui

import encryption
from data import Data
import settings

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

def getLastUsedFile(fullPath = False) -> str:
    if not os.path.isfile("lastUsedFile.txt"):
        return None
    with open("lastUsedFile.txt", "r") as f:
        if fullPath:
            return os.path.join(userDataDir, f.read() + settings.extension)
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
    # check if file already exists
    if os.path.isfile(os.path.join(userDataDir, fileName + settings.extension)):
        easygui.msgbox("A file with the name '"+fileName+"' already exists. Please choose another name.", "Password Manager")
        return False
    return True

def isUserDataDirEmpty() -> bool:
    return len(os.listdir(userDataDir)) == 0

def createEncryptedFile(fileName, password):
    open(os.path.join(userDataDir, fileName + settings.extension), 'wb').close()
    saveLastUsedFile(fileName)
    encryption.encrypt_file(Data().byteData, os.path.join(userDataDir, fileName + settings.extension), password)

#check if only .enc files are in the userData directory
def checkUserDataValidity() -> tuple[bool, str]:
    for object in os.listdir(userDataDir):
        if not os.path.isfile(os.path.join(userDataDir, object)) or not object.endswith(settings.extension):
            return (False, object)
    return (True, None)


def getAllFilesInDir(directory, fullPath = False) -> list:
    files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            if fullPath:
                files.append(os.path.join(directory, file))
            else:
                files.append(file)
    return files