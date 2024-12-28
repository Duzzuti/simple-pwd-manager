import traceback
import pandas as pd
import easygui
import os
from io import StringIO

import settings
import encryption
from sys import exit

class Data:
    def __init__(self):
        self.pwd = pd.DataFrame({"Website": [], "Email": [], "Username": [], "Password": []})
        self.other = pd.DataFrame({"Name": [], "Info": []})
        self.calculateByteData()

        # holds full filepath to the encrypted file
        self.filepath = None
        # holds the password for the encrypted file
        self.password = None
    
    @classmethod
    def fromBytes(self, byteData: bytes):
        if len(byteData) < settings.pwdLenBytes:
            return None
        data = self()
        data.byteData = byteData
        try:
            randomLength = byteData[0]
            pos = 1
            randomBytes = byteData[pos:pos+randomLength]
            pos += randomLength
            lenPwd = int.from_bytes(byteData[pos:pos+settings.pwdLenBytes], byteorder="big", signed=False)
            pos += settings.pwdLenBytes
        
            data.pwd = pd.read_csv(StringIO(byteData[pos:pos+lenPwd].decode()), index_col=False)
            data.other = pd.read_csv(StringIO(byteData[pos+lenPwd:].decode()), index_col=False)
        except IndexError:
            easygui.msgbox("The file is corrupted. The format is not as expected.", "Password Manager")
            traceback.print_exc()
            exit()
        return data

    def setMeta(self, filepath: str, password: str):
        self.filepath = filepath
        self.password = password
    
    def requireMeta(self):
        if self.filepath is None or self.password is None:
            easygui.msgbox("Meta data is required for this action.", "Password Manager")
            exit()
    
    def calculateByteData(self):
        pwdBytes = self.pwd.to_csv(index=False).encode()
        otherBytes = self.other.to_csv(index=False).encode()
        randomLength = os.urandom(1)
        randomBytes = os.urandom(int.from_bytes(randomLength, byteorder="big", signed=False))
        self.byteData = \
            randomLength + \
            randomBytes + \
            encryption.intToBytes(len(pwdBytes), settings.pwdLenBytes) + \
            pwdBytes + \
            otherBytes

    def addPwdToData(self, website: str, email: str, username: str, password: str):
        self.pwd = pd.concat([self.pwd, pd.DataFrame({"Website": [website], "Email": [email], "Username": [username], "Password": [password]})], ignore_index=True)
        self.calculateByteData()
    
    def addOtherToData(self, name: str, info: str):
        self.other = pd.concat([self.other, pd.DataFrame({"Name": [name], "Info": [info]})], ignore_index=True)
        self.calculateByteData()

    def showPwd(self):
        # print full df without index sorted by website
        if len(self.pwd) == 0:
            easygui.msgbox("No logins found.", "Password Manager")
        else:
            print(self.pwd.sort_values(by="Website").rename(columns={"Website": "Website/App"}, inplace=False).to_string(index=False))
            input("Press Enter to clear...")
            os.system('cls' if os.name == 'nt' else 'clear')
    
    def showOther(self):
        if len(self.other) == 0:
            easygui.msgbox("No other information found.", "Password Manager")
        else:
            print(self.other.sort_values(by="Name").to_string(index=False))
            input("Press Enter to clear...")
            os.system('cls' if os.name == 'nt' else 'clear')
    
    def addPwd(self):
        self.requireMeta()
        # asks the user for new password data and adds it to the Dataframe
        while True:
            dataAddPwd = easygui.multenterbox("Enter the following information: ", "Password Manager", ["Website/App (required)", "Email", "Username", "Password (required)"])
            if dataAddPwd is None:
                break
            elif dataAddPwd[0] == "" or dataAddPwd[3] == "":
                easygui.msgbox("A website/app and a password is required.", "Password Manager")
            else:
                if dataAddPwd[0] in self.pwd["Website"].values:
                    # get all emails and usernames as strings
                    emails = self.pwd[self.pwd["Website"] == dataAddPwd[0]]["Email"].values
                    usernames = self.pwd[self.pwd["Website"] == dataAddPwd[0]]["Username"].values
                    emailsPlusUsernames = "\n".join(["Mail:" + emails[i] + ", User:" + usernames[i] for i in range(len(emails))])

                    userConfirm = easygui.ynbox("An entry for this website/app already exists. Do you want to add the information as an other login? (No does NOT safe the new information). \n" + \
                                                "If you want to change old information (e.g. a single password) please use the 'Change password' section of the main menu.\n\n" + \
                                                "Current information for " + dataAddPwd[0] + ":\n" +
                                                emailsPlusUsernames + \
                                                "\nNew information:\n" + \
                                                "Mail:" + dataAddPwd[1] + ", User:" + dataAddPwd[2] + "\n", "Password Manager")
                    if not userConfirm:
                        continue
                self.addPwdToData(dataAddPwd[0], dataAddPwd[1], dataAddPwd[2], dataAddPwd[3])
                encryption.encrypt_file(self.byteData, self.filepath, self.password)
                break
    
    def addOther(self):
        self.requireMeta()
        while True:
            otherName = easygui.enterbox("Enter a name for the information you want to add. This is only for your reference.", "Password Manager")
            if otherName is None:
                break
            elif otherName == "":
                easygui.msgbox("A name is required.", "Password Manager")
                continue
            while True:
                otherInfo = easygui.textbox("Store any information you want for " + otherName, "Password Manager")
                if otherInfo is None:
                    break
                elif otherInfo == "":
                    easygui.msgbox("The information is required.", "Password Manager")
                    continue
                else:
                    self.addOtherToData(otherName, otherInfo)
                    encryption.encrypt_file(self.byteData, self.filepath, self.password)
                    break
            break
    
    def changeData(self):
        self.requireMeta()
        if len(self.pwd) == 0:
            easygui.msgbox("No logins found.", "Password Manager")
        elif len(self.pwd) == 1:
            choice = [self.pwd["Website"].values[0]]
        else:
            choice = easygui.multchoicebox("Choose the websites/apps to delete or change the information for: ", "Password Manager", self.pwd["Website"].sort_values().tolist())
        if choice is not None:
            for i in choice:
                choiceAction = easygui.buttonbox("Choose an action for " + i + ": ", "Password Manager", ["Delete", "Change Information", "Skip"])
                if choiceAction == "Skip" or choiceAction is None:
                    continue
                elif choiceAction == "Delete":
                    self.pwd = self.pwd[self.pwd["Website"] != i]
                    self.calculateByteData()
                elif choiceAction == "Change Information":
                    while True:
                        newData = easygui.multenterbox("Enter the following information: ", "Password Manager", ["Website/App (required)", "Email", "Username", "Password (required)"], [i, self.pwd[self.pwd["Website"] == i]["Email"].values[0], self.pwd[self.pwd["Website"] == i]["Username"].values[0], self.pwd[self.pwd["Website"] == i]["Password"].values[0]])
                        if newData[0] == "" or newData[3] == "":
                            easygui.msgbox("A website/app and a password is required.", "Password Manager")
                        else:
                            break
                    if newData is not None:
                        self.pwd = self.pwd[self.pwd["Website"] != i]
                        self.addPwdToData(newData[0], newData[1], newData[2], newData[3])
                encryption.encrypt_file(self.byteData, self.filepath, self.password)
        