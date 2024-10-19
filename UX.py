import easygui
import os

import structureTools
import encryption

# let the user create a new file and returns (filePath, password)
def newFileHandler() -> tuple[str, str]:
    while True:
        newFileName = easygui.enterbox("No encrypted password file found. Do you want to create a new one?", "Password Manager", structureTools.defaultEncFileWithoutExt)
        if newFileName is None:
            exit()
        if structureTools.verifyFileName(newFileName):
            break
    while True:
        password = easygui.passwordbox("Enter a master password for the file: ", "Password Manager")
        if password is None:
            exit()
        if not password:
            easygui.msgbox("A non empty password is required.", "Password Manager")
            continue
        # confirm password
        passwordConfirm = easygui.passwordbox("Confirm the master password: ", "Password Manager")
        if passwordConfirm is None:
            exit()
        if(password == passwordConfirm):
            break
        easygui.msgbox("Passwords do not match. Try again.", "Password Manager")

    tmpUserInp = easygui.msgbox("MAKE SURE TO REMEMBER THE PASSWORD. THERE IS NO WAY TO RECOVER IT.\nIF YOU FORGET THE PASSWORD, ALL DATA IN THE FILE WILL BE LOST.", "Password Manager")
    if tmpUserInp is None:
        exit()
    showPwd = easygui.ynbox("Show password?\nPLEASE NOTE THAT THIS WILL SHOW SENSITIVE DATA TO THE SCREEN", "Password Manager", ("Yes", "No"))
    if showPwd is None:
        exit()
    if showPwd:
        easygui.msgbox("Your password is: " + password, "Password Manager")
    userPwdSafeConfirm = easygui.ynbox("Make sure to save the password somewhere safe. Please confirm.", "Password Manager")
    while not userPwdSafeConfirm:
        if userPwdSafeConfirm is None:
            exit()
        userPwdSafeConfirm = easygui.ynbox("You have to confirm before you can continue. Please make sure to have your password backed up somewhere.", "Password Manager")
    print("Creating new encrypted password file...")
    structureTools.createEncryptedFile(newFileName, password)
    #TODO, new login?
    easygui.msgbox("Welcome to the password manager\nYou can enter your password data in this interface\nThe data will be encrypted with the master password and stored in the file (" + newFileName + ")\nYou should do a backup of the file regularly to avoid losing data\nIf you lose the file, you will lose all data in it", "Password Manager")
    return os.path.join(structureTools.userDataDir, newFileName + ".enc"), password

def chooseEncFile(encFiles: list[str]) -> str:
    if len(encFiles) == 1:
        return encFiles[0]
    fileName = easygui.choicebox("Choose a file to open: ", "Password Manager", encFiles)
    if fileName is None:
        exit()
    return os.path.join(structureTools.userDataDir, fileName + ".enc")

# TODO return data too?
def getPassword(filePath: str) -> str:
    while True:
        password = easygui.passwordbox("Enter the master password for the file ("+filePath+"): ", "Password Manager")
        if password is None:
            exit()
        dataBytes = encryption.decrypt_file(filePath, password)
        while(not dataBytes):
            password = easygui.passwordbox("Wrong password for file ("+filePath+"). Try again: ", "Password Manager")
            if password is None:
                exit()
            dataBytes = encryption.decrypt_file(filePath, password)
        #     data = data[len(correct_bytes):]
        return password