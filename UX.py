import easygui
import os
import tkinter as tk

import structureTools
import encryption
import settings

def createPasswordWindow(text: str, title: str, encFiles: list[str], filePath: str) -> tuple[str, str]:
    retCode = "CANCEL"
    result = None
    def onSubmit():
        nonlocal retCode, result
        result = password_entry.get()
        root.destroy()
        retCode, result = "OK", result

    def onChangeFile():
        nonlocal retCode, result
        root.destroy()
        newPath = chooseEncFile(encFiles, preselectFile=filePath)
        if len(encFiles) == 1:
            easygui.msgbox("No other files found in directory (" + structureTools.userDataDir + "/)", "Password Manager")
        retCode, result = "CHANGE", newPath
    
    def onNewFile():
        nonlocal retCode, result
        root.destroy()
        retCode, result = "NEW", None
    
    root = tk.Tk()
    root.title(title)
    # root.geometry("386x127")
    # set window to screen position 300 x 200
    root.geometry("+300+200")
    root.resizable(True, True)
    root.option_add("*Font", "Helvetica 12")

    # Password entry label, make it auto adjust to text
    label = tk.Label(root, text=text)
    label.pack(pady=10)
    # adjust on resize
    root.bind("<Configure>", lambda e: label.config(wraplength=root.winfo_width()-20))

    # Password entry field with full width
    password_entry = tk.Entry(root, show="*", width=40)
    password_entry.pack(pady=5, padx=10)
    password_entry.focus_force()

    # Submit Button
    submitButton = tk.Button(root, text="OK", command=onSubmit)
    submitButton.pack(side="left", padx=20, pady=10)
    # make submit button activate on enter
    root.bind("<Return>", lambda e: submitButton.invoke())

    # Cancel Button
    cancelButton = tk.Button(root, text="Cancel", command=root.destroy)
    cancelButton.pack(side="left", padx=20, pady=10)
    # make cancel button activate on escape
    root.bind("<Escape>", lambda e: cancelButton.invoke())

    # Change File Button
    changeFileButton = tk.Button(root, text="Change File", command=onChangeFile)
    changeFileButton.pack(side="right", padx=20, pady=10)

    # New File Button
    newFileButton = tk.Button(root, text="New File", command=onNewFile)
    newFileButton.pack(side="right", padx=20, pady=10)

    root.mainloop()
    return (retCode, result)


# let the user create a new file and returns (filePath, password)
def newFileHandler(noFileFound=False) -> tuple[str, str]:
    while True:
        if noFileFound:
            msg = "No encrypted password file found. Creating a new file...\nEnter file name:"
        else:
            msg = "Enter new file name:"
        newFileName = easygui.enterbox(msg, "Password Manager", structureTools.defaultEncFileWithoutExt)
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
        userPwdSafeConfirm = easygui.ynbox("You have to confirm before you can continue. Please make sure your password is backed up somewhere.", "Password Manager")
    print("Creating new encrypted password file...")
    structureTools.createEncryptedFile(newFileName, password)
    easygui.msgbox("Welcome to the password manager\nYou can enter your login data in this interface\nThe data will be encrypted with the master password and stored in the file (" + newFileName + ")\nYou should do a backup of the file regularly to avoid losing data\nIf you lose the file, you will lose all data in it", "Password Manager")
    return (os.path.join(structureTools.userDataDir, newFileName + settings.extension), password)

def chooseEncFile(encFiles: list[str], isFullPath = True, preselectFile: str = None) -> str:
    preselectIndex = 0
    if len(encFiles) == 1:
        return encFiles[0]
    if preselectFile is not None:
        if preselectFile not in encFiles:
            print("Error in chooseEncFile: preselectFile ("+preselectFile+") not in encFiles")
            exit()
        # get index of preselectFile
        preselectIndex = encFiles.index(preselectFile)
    fileName = easygui.choicebox("Choose a file to open: ", "Password Manager", encFiles, preselectIndex)
    if fileName is None:
        exit()
    if isFullPath:
        return fileName
    return os.path.join(structureTools.userDataDir, fileName + settings.extension)

def getPassword(filePath: str, encFiles: list[str]) -> tuple[str, str, bytes]:
    while True:
        retCode, result = createPasswordWindow("Enter the master password for the file ("+filePath+"): ", "Password Manager", encFiles, filePath)
        if retCode == "CANCEL":
            exit()
        elif retCode == "CHANGE":
            filePath = result
        elif retCode == "NEW":
            newFilePath, newPassword = newFileHandler()
            return (newFilePath, newPassword, None)
        elif retCode == "OK":
            password = result
            if password is None:
                exit()
            dataBytes = encryption.decrypt_file(filePath, password)
            while(not dataBytes):
                password = easygui.passwordbox("Wrong password for file ("+filePath+"). Try again: ", "Password Manager")
                if password is None:
                    exit()
                dataBytes = encryption.decrypt_file(filePath, password)
            structureTools.saveLastUsedFile(os.path.basename(filePath)[:-len(settings.extension)])
            return (filePath, password, dataBytes)
        else:
            print("Error in getPassword: Invalid return code: " + retCode)
            exit()
