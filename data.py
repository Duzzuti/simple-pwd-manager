import traceback
import pandas as pd
import easygui
import os
from io import StringIO

import settings
from settings import language
import encryption
from basic_UX import enterBox, ynBox
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
            easygui.msgbox(language.ERR_FILE_CORRUPTED_FORMAT, "Password Manager")
            traceback.print_exc()
            exit()
        return data

    def setMeta(self, filepath: str, password: str):
        self.filepath = filepath
        self.password = password
    
    def requireMeta(self):
        if self.filepath is None or self.password is None:
            easygui.msgbox(language.ERR_META_REQUIRED, "Password Manager")
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
            easygui.msgbox(language.NO_LOGINS_FOUND, "Password Manager")
        else:
            print(self.pwd.sort_values(by="Website").rename(columns={
                "Website": language.WEBSITE_APP, 
                "Email": language.EMAIL, 
                "Username": language.USERNAME, 
                "Password": language.PASSWORD
                }, inplace=False).to_string(index=False))
            input(language.ENTER_TO_CLEAR)
            os.system('cls' if os.name == 'nt' else 'clear')
    
    def showOther(self):
        if len(self.other) == 0:
            easygui.msgbox(language.NO_OTHER_INFO_FOUND, "Password Manager")
        else:
            print(self.other.sort_values(by="Name").rename(columns={
                "Name": language.INFO_TITLE,
                "Info": language.INFO_CONTENT
                }, inplace=False).to_string(index=False))
            input(language.ENTER_TO_CLEAR)
            os.system('cls' if os.name == 'nt' else 'clear')
    
    def addPwd(self):
        self.requireMeta()
        # asks the user for new password data and adds it to the Dataframe
        while True:
            dataAddPwd = easygui.multenterbox(language.ENTER_FOLLOWING, "Password Manager", 
                [language.WEBSITE_APP + " " + language.REQUIRED, language.EMAIL, language.USERNAME, language.PASSWORD + " " + language.REQUIRED])
            if dataAddPwd is None:
                break
            elif dataAddPwd[0] == "" or dataAddPwd[3] == "":
                easygui.msgbox(language.WEBSITE_PASSWORD_REQUIRED, "Password Manager")
            else:
                if dataAddPwd[0] in self.pwd["Website"].values:
                    # get all emails and usernames as strings
                    emails = self.pwd[self.pwd["Website"] == dataAddPwd[0]]["Email"].values
                    usernames = self.pwd[self.pwd["Website"] == dataAddPwd[0]]["Username"].values
                    emailsPlusUsernames = "\n".join([language.EMAIL + ":" + emails[i] + ", " + language.USERNAME + ":" + usernames[i] for i in range(len(emails))])

                    userConfirm = ynBox(language.PASSWORD_ENTRY_ALREADY_EXISTS_MESSAGE +
                                                language.CURRENT_LOGINS_FOR + dataAddPwd[0] + ":\n" +
                                                emailsPlusUsernames + "\n" + language.NEW_INFORMATION + ":\n" +
                                                language.EMAIL + ":" + dataAddPwd[1] + ", " + language.USERNAME + ":" + dataAddPwd[2] + "\n", "Password Manager")
                    if not userConfirm:
                        continue
                self.addPwdToData(dataAddPwd[0], dataAddPwd[1], dataAddPwd[2], dataAddPwd[3])
                encryption.encrypt_file(self.byteData, self.filepath, self.password)
                break
    
    def addOther(self):
        self.requireMeta()
        while True:
            otherName = enterBox(language.ADD_INFO_TITLE, "Password Manager")
            if otherName is None:
                break
            elif otherName == "":
                easygui.msgbox(language.INFO_TITLE_REQUIRED, "Password Manager")
                continue
            while True:
                otherInfo = easygui.textbox(language.STORE_INFORMATION_FOR + otherName, "Password Manager")
                if otherInfo is None:
                    break
                elif otherInfo == "":
                    easygui.msgbox(language.INFO_CONTENT_REQUIRED, "Password Manager")
                    continue
                else:
                    self.addOtherToData(otherName, otherInfo)
                    encryption.encrypt_file(self.byteData, self.filepath, self.password)
                    break
            break
    
    def changeData(self):
        self.requireMeta()
        if len(self.pwd) == 0:
            easygui.msgbox(language.NO_LOGINS_FOUND, "Password Manager")
        elif len(self.pwd) == 1:
            choice = [self.pwd["Website"].values[0]]
        else:
            choice = easygui.multchoicebox(language.CHOOSE_WEBSITE_TO_CHANGE_DELETE, "Password Manager", self.pwd["Website"].sort_values().tolist())
        if choice is not None:
            for i in choice:
                choiceAction = easygui.buttonbox(language.CHOOSE_ACTION_FOR + i + ": ", "Password Manager", [language.DELETE, language.CHANGE_INFORMATION, language.SKIP])
                if choiceAction == language.SKIP or choiceAction is None:
                    continue
                elif choiceAction == language.DELETE:
                    self.pwd = self.pwd[self.pwd["Website"] != i]
                    self.calculateByteData()
                elif choiceAction == language.CHANGE_INFORMATION:
                    while True:
                        newData = easygui.multenterbox(language.ENTER_FOLLOWING, "Password Manager", 
                            [language.WEBSITE_APP + " " + language.REQUIRED, language.EMAIL, language.USERNAME, language.PASSWORD + " " + language.REQUIRED], 
                            [i, self.pwd[self.pwd["Website"] == i]["Email"].values[0], self.pwd[self.pwd["Website"] == i]["Username"].values[0], self.pwd[self.pwd["Website"] == i]["Password"].values[0]])
                        if newData[0] == "" or newData[3] == "":
                            easygui.msgbox(language.WEBSITE_PASSWORD_REQUIRED, "Password Manager")
                        else:
                            break
                    if newData is not None:
                        self.pwd = self.pwd[self.pwd["Website"] != i]
                        self.addPwdToData(newData[0], newData[1], newData[2], newData[3])
                encryption.encrypt_file(self.byteData, self.filepath, self.password)
        