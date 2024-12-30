import os
import easygui

import network
import structureTools
from data import Data
import UX

# init the file structure and exits if there are any problems
structureTools.init()
lastUsedFile = structureTools.getLastUsedFile(fullPath=True)
encFiles = structureTools.getAllFilesInDir(structureTools.userDataDir, fullPath=True)

network.check_for_updates(threaded=True)

# SELECT AND DECRYPT FILE
password = None
filePath = None
byteData = None
# no file found, create new file
if len(encFiles) == 0:
    filePath, password = UX.newFileHandler(noFileFound=True)
# no last used file found
elif lastUsedFile is None:
    filePath = UX.chooseEncFile(encFiles)
    filePath, password, byteData = UX.getPassword(filePath, encFiles)
# last used file found
elif os.path.isfile(lastUsedFile):
    filePath = lastUsedFile
    filePath, password, byteData = UX.getPassword(filePath, encFiles)
# last used file not found
else:
    tmp = easygui.msgbox("The last used file ("+lastUsedFile+") was not found. Copy the file back to the location or choose an other file to open", "Password Manager")
    if tmp is None:
        exit()
    filePath = UX.chooseEncFile(encFiles)
    filePath, password, byteData = UX.getPassword(filePath, encFiles)

# new file was created
if byteData == None:
    byteData = Data().byteData

if not byteData:
    easygui.msgbox("The password file could not be decrypted. Please try again.", "Password Manager")
    exit()
data = Data.fromBytes(byteData)
data.setMeta(filePath, password)

while True:
    user_choice = easygui.buttonbox("Choose an action: ", "Password Manager", ["Show logins", "Add login", "Show other", "Add other", "Delete/Change login", "Exit"])
    if user_choice == "Show logins":
        data.showPwd()
    elif user_choice == "Add login":
        data.addPwd()
    # todo show other information in good format
    elif user_choice == "Show other":
        data.showOther()
    # todo handle multiple entries with the same name
    elif user_choice == "Add other":
        data.addOther()
    elif user_choice == "Delete/Change login":
        data.changeData()
    elif user_choice == "Exit" or user_choice is None:
        break