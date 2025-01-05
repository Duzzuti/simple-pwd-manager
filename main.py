try:
    from settings import language

    import os
    import easygui

    import network
    import structureTools
    from data import Data
    import UX
except ImportError:
    print(language.ERR_MISSING_DEPENDENCIES)
    import dependencies
    if(dependencies.installDependencies()):
        input(language.RESTART_ENTER_TO_EXIT)
    os._exit(0)

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
    tmp = easygui.msgbox(language.ERR_LAST_USED_FILE_NOT_FOUND1 + lastUsedFile + language.ERR_LAST_USED_FILE_NOT_FOUND2, "Password Manager")
    if tmp is None:
        exit()
    filePath = UX.chooseEncFile(encFiles)
    filePath, password, byteData = UX.getPassword(filePath, encFiles)

# new file was created
if byteData == None:
    byteData = Data().byteData

if not byteData:
    easygui.msgbox(language.ERR_FILE_COULD_NOT_BE_DECRYPTED, "Password Manager")
    exit()
data = Data.fromBytes(byteData)
data.setMeta(filePath, password)

while True:
    user_choice = easygui.buttonbox(language.CHOOSE_ACTION, "Password Manager", [
        language.SHOW_LOGINS, language.ADD_LOGIN, language.SHOW_OTHER, language.ADD_OTHER, language.DELETE_CHANGE_LOGIN, language.EXIT])
    if user_choice == language.SHOW_LOGINS:
        data.showPwd()
    elif user_choice == language.ADD_LOGIN:
        data.addPwd()
    # TODO show other information in good format
    elif user_choice == language.SHOW_OTHER:
        data.showOther()
    # TODO handle multiple entries with the same name
    elif user_choice == language.ADD_OTHER:
        data.addOther()
    elif user_choice == language.DELETE_CHANGE_LOGIN:
        data.changeData()
    elif user_choice == language.EXIT or user_choice is None:
        break