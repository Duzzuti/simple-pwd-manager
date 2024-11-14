import easygui
import os

import structureTools
import encryption
import settings

# def create_password_window():
#     def onSubmit():
#         result = password_entry.get()
#         root.destroy()
#         return result

#     def onChangeFile():
#         root.destroy()
#         chooseEncFile(encFiles)
    
#     root = tk.Tk()
#     root.title("Password Box")
#     root.geometry("300x150")
#     root.resizable(True, True)
#     result = None

#     # Password entry label
#     label = tk.Label(root, text="Enter Password:")
#     label.pack(pady=10)

#     # Password entry field
#     password_entry = tk.Entry(root, show="*", width=30)
#     password_entry.pack(pady=5)

#     # Button 1
#     button1 = tk.Button(root, text="OK", command=lambda: result = onSubmit())
#     button1.pack(side="left", padx=20, pady=20)

#     # Button 2
#     button2 = tk.Button(root, text="Cancel", command=root.destroy)
#     button2.pack(side="left", padx=20, pady=20)

#     # Adjustable Button 3
#     button3_text = "Change File"
#     button3 = tk.Button(root, text=button3_text, command=onChangeFile)
#     button3.pack(side="left", padx=20, pady=20)

#     root.mainloop()
#     return result


# let the user create a new file and returns (filePath, password)
def newFileHandler() -> tuple[str, str]:
    while True:
        newFileName = easygui.enterbox("No encrypted password file found. Do you want to create a new one?\nEnter file name:", "Password Manager", structureTools.defaultEncFileWithoutExt)
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
    easygui.msgbox("Welcome to the password manager\nYou can enter your password data in this interface\nThe data will be encrypted with the master password and stored in the file (" + newFileName + ")\nYou should do a backup of the file regularly to avoid losing data\nIf you lose the file, you will lose all data in it", "Password Manager")
    return os.path.join(structureTools.userDataDir, newFileName + settings.extension), password

def chooseEncFile(encFiles: list[str], isFullPath = True) -> str:
    if len(encFiles) == 1:
        return encFiles[0]
    fileName = easygui.choicebox("Choose a file to open: ", "Password Manager", encFiles)
    if fileName is None:
        exit()
    if isFullPath:
        return fileName
    return os.path.join(structureTools.userDataDir, fileName + settings.extension)

def getPassword(filePath: str) -> tuple[str, bytes]:
    while True:
        password = easygui.passwordbox("Enter the master password for the file ("+filePath+"): ", "Password Manager")
        #create_password_window()
        if password is None:
            exit()
        dataBytes = encryption.decrypt_file(filePath, password)
        while(not dataBytes):
            password = easygui.passwordbox("Wrong password for file ("+filePath+"). Try again: ", "Password Manager")
            if password is None:
                exit()
            dataBytes = encryption.decrypt_file(filePath, password)
        structureTools.saveLastUsedFile(os.path.basename(filePath)[:-len(settings.extension)])
        return [password, dataBytes]
