import os
import easygui
import pandas as pd
import pickle

import structureTools
import UX

# init the file structure and exits if there are any problems
structureTools.init()

if structureTools.isUserDataDirEmpty():
    UX.newFileHandler()
else:
    password = easygui.passwordbox("A password file was found ("+file+"). Enter the master password to continue: ", "Password Manager")
    if password is None:
        exit()
    data = decrypt_file(file, password)
    while(len(data) < len(correct_bytes) or data[:len(correct_bytes)] != correct_bytes):
        password = easygui.passwordbox("Wrong password for file ("+file+"). Try again: ", "Password Manager")
        if password is None:
            exit()
        data = decrypt_file(file, password)
    data = data[len(correct_bytes):]

df_pwd : pd.DataFrame = pickle.loads(data)[0]
df_info : pd.DataFrame = pickle.loads(data)[1]

while True:
    user_choice = easygui.buttonbox("Choose an action: ", "Password Manager", ["Show passwords", "Add password", "Show other", "Add other", "Delete/Change Password", "Exit"])
    if user_choice == "Show passwords":
        # print full df without index sorted by website
        if len(df_pwd) == 0:
            easygui.msgbox("No websites found.", "Password Manager")
            continue
        print(df_pwd.sort_values(by="Website").to_string(index=False))
        input("Press Enter to clear...")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif user_choice == "Add password":
        while True:
            data_addpwd = easygui.multenterbox("Enter the following information: ", "Password Manager", ["Website", "Email", "Username", "Password"])
            if data_addpwd is None:
                break
            elif data_addpwd[0] == "" or data_addpwd[3] == "":
                easygui.msgbox("A website and a password is required.", "Password Manager")
            else:
                if data_addpwd[0] in df_pwd["Website"].values:
                    # get all emails and usernames as strings
                    emails = df_pwd[df_pwd["Website"] == data_addpwd[0]]["Email"].values
                    usernames = df_pwd[df_pwd["Website"] == data_addpwd[0]]["Username"].values
                    emails_plus_usernames = "\n".join(["Mail:" + emails[i] + ", User:" + usernames[i] for i in range(len(emails))])

                    user_confirm = easygui.ynbox("The website already exists. Do you want to add the information as an other login? (No does NOT safe the new information). \n" + \
                                                "If you want to change old information (e.g. a single password) please use the 'Change password' section of the main menu.\n\n" + \
                                                "Current information for " + data_addpwd[0] + ":\n" +
                                                emails_plus_usernames + \
                                                "\nNew information:\n" + \
                                                "Mail:" + data_addpwd[1] + ", User:" + data_addpwd[2] + "\n", "Password Manager")
                    if not user_confirm:
                        continue
                df_pwd = pd.concat([df_pwd, pd.DataFrame({"Website": [data_addpwd[0]], "Email": [data_addpwd[1]], "Username": [data_addpwd[2]], "Password": [data_addpwd[3]]})], ignore_index=True)
                encrypt_pdata(pickle.dumps([df_pwd, df_info]), file, password)
                break
    # todo show other information in good format
    elif user_choice == "Show other":
        if len(df_info) == 0:
            easygui.msgbox("No other information found.", "Password Manager")
            continue
        print(df_info.to_string(index=False))
        input("Press Enter to clear...")
        os.system('cls' if os.name == 'nt' else 'clear')

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