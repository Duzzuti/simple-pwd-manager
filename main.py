import os
import easygui
import pandas as pd
import pickle

import structureTools
import encryption
from data import Data
import UX

# init the file structure and exits if there are any problems
structureTools.init()
lastUsedFile = structureTools.getLastUsedFile(fullPath=True)
encFiles = structureTools.getAllFilesInDir(structureTools.userDataDir, fullPaths=True)


# SELECT AND DECRYPT FILE
password = None
filePath = None
# no file found, create new file
if len(encFiles) == 0:
    filePath, password = UX.newFileHandler()
# no last used file found
elif lastUsedFile is None:
    filePath = UX.chooseEncFile(encFiles)
    password = UX.getPassword(filePath)
# last used file found
elif os.path.isfile(lastUsedFile):
    filePath = lastUsedFile
    password = UX.getPassword(filePath)
# last used file not found
else:
    tmp = easygui.msgbox("The last used file ("+lastUsedFile+") was not found. Copy the file back to the location or choose an other file to open", "Password Manager")
    if tmp is None:
        exit()
    filePath = UX.chooseEncFile(encFiles)
    password = UX.getPassword(filePath)

data = encryption.decrypt_file(filePath, password)
if not data:
    easygui.msgbox("The password file could not be decrypted. Please try again.", "Password Manager")
    exit()
data : Data = pickle.loads(data)

while True:
    user_choice = easygui.buttonbox("Choose an action: ", "Password Manager", ["Show passwords", "Add password", "Show other", "Add other", "Delete/Change Password", "Exit"])
    if user_choice == "Show passwords":
        data.showPwd()
    elif user_choice == "Add password":
        data.addPwd()
    # todo show other information in good format
    elif user_choice == "Show other":
        data.showOther()
    # todo handle multiple entries with the same name
    elif user_choice == "Add other":
        while True:
            other_name = easygui.enterbox("Enter a name for the information you want to add. This is only for your reference.", "Password Manager")
            if other_name is None:
                break
            elif other_name == "":
                easygui.msgbox("A name is required.", "Password Manager")
                continue
            while True:
                other_info = easygui.textbox("Store any information you want for " + other_name, "Password Manager") #Not empty
                if other_info is None:
                    break
                elif other_info == "":
                    easygui.msgbox("The information is required.", "Password Manager")
                    continue
                else:
                    df_info = pd.concat([df_info, pd.DataFrame({"Name": [other_name], "Info": [other_info]})], ignore_index=True)
                    encrypt_pdata(pickle.dumps([df_pwd, df_info]), file, password)
                    break
            break
    elif user_choice == "Delete/Change Password":
        # if there is only one website, delete it
        if len(df_pwd) == 0:
            easygui.msgbox("No websites found.", "Password Manager")
            continue
        elif len(df_pwd) == 1:
            choice_dc = [df_pwd["Website"].values[0]]
        else:
            choice_dc = easygui.multchoicebox("Choose the websites to delete or change the information for: ", "Password Manager", df_pwd["Website"].sort_values().tolist())
        if choice_dc is not None:
            for i in choice_dc:
                user_dc = easygui.buttonbox("Choose an action for " + i + ": ", "Password Manager", ["Delete", "Change Information", "Skip"])
                if user_dc == "Skip" or user_dc is None:
                    continue
                elif user_dc == "Delete":
                    df_pwd = df_pwd[df_pwd["Website"] != i]
                elif user_dc == "Change Information":
                    while True:
                        data_addpwd = easygui.multenterbox("Enter the following information: ", "Password Manager", ["Website", "Email", "Username", "Password"], [i, df_pwd[df_pwd["Website"] == i]["Email"].values[0], df_pwd[df_pwd["Website"] == i]["Username"].values[0], df_pwd[df_pwd["Website"] == i]["Password"].values[0]])
                        if data_addpwd[0] == "" or data_addpwd[3] == "":
                            easygui.msgbox("A website and a password is required.", "Password Manager")
                        else:
                            break
                    if data_addpwd is not None:
                        df_pwd = df_pwd[df_pwd["Website"] != i]
                        df_pwd = pd.concat([df_pwd, pd.DataFrame({"Website": [data_addpwd[0]], "Email": [data_addpwd[1]], "Username": [data_addpwd[2]], "Password": [data_addpwd[3]]})], ignore_index=True)
            encrypt_pdata(pickle.dumps([df_pwd, df_info]), file, password)

    elif user_choice == "Exit" or user_choice is None:
        break