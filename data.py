import pandas as pd
import easygui
import os
from io import StringIO
import settings

class Data:
    def __init__(self):
        self.pwd = pd.DataFrame({"Website": [], "Email": [], "Username": [], "Password": []})
        self.other = pd.DataFrame({"Name": [], "Info": []})
        self.calculateByteData()
    
    @classmethod
    def fromBytes(self, byteData: bytes):
        if len(byteData) < settings.pwdLenBytes:
            return None
        data = self()
        data.byteData = byteData
        lenPwd = int.from_bytes(byteData[:settings.pwdLenBytes], byteorder="big", signed=False)
        data.pwd = pd.read_csv(StringIO(byteData[settings.pwdLenBytes:settings.pwdLenBytes+lenPwd].decode()), index_col=False)
        data.other = pd.read_csv(StringIO(byteData[settings.pwdLenBytes+lenPwd:].decode()), index_col=False)
        return data
    
    def calculateByteData(self):
        pwdBytes = self.pwd.to_csv(index=False).encode()
        otherBytes = self.other.to_csv(index=False).encode()
        self.byteData = len(pwdBytes).to_bytes(settings.pwdLenBytes, signed=False, byteorder="big") + pwdBytes + otherBytes

    def addPwdToData(self, website: str, email: str, username: str, password: str):
        self.pwd = pd.concat([self.pwd, pd.DataFrame({"Website": [website], "Email": [email], "Username": [username], "Password": [password]})], ignore_index=True)
        self.calculateByteData()
    
    def addOtherToData(self, name: str, info: str):
        self.other = pd.concat([self.other, pd.DataFrame({"Name": [name], "Info": [info]})], ignore_index=True)
        self.calculateByteData()

    def showPwd(self):
        # print full df without index sorted by website
        if len(self.pwd) == 0:
            easygui.msgbox("No websites found.", "Password Manager")
        else:
            print(self.pwd.sort_values(by="Website").to_string(index=False))
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
        # asks the user for new password data and adds it to the dataframe
        while True:
            dataAddPwd = easygui.multenterbox("Enter the following information: ", "Password Manager", ["Website", "Email", "Username", "Password"])
            if dataAddPwd is None:
                break
            elif dataAddPwd[0] == "" or dataAddPwd[3] == "":
                easygui.msgbox("A website and a password is required.", "Password Manager")
            else:
                if dataAddPwd[0] in self.pwd["Website"].values:
                    # get all emails and usernames as strings
                    emails = self.pwd[self.pwd["Website"] == dataAddPwd[0]]["Email"].values
                    usernames = self.pwd[self.pwd["Website"] == dataAddPwd[0]]["Username"].values
                    emailsPlusUsernames = "\n".join(["Mail:" + emails[i] + ", User:" + usernames[i] for i in range(len(emails))])

                    userConfirm = easygui.ynbox("The website already exists. Do you want to add the information as an other login? (No does NOT safe the new information). \n" + \
                                                "If you want to change old information (e.g. a single password) please use the 'Change password' section of the main menu.\n\n" + \
                                                "Current information for " + dataAddPwd[0] + ":\n" +
                                                emailsPlusUsernames + \
                                                "\nNew information:\n" + \
                                                "Mail:" + dataAddPwd[1] + ", User:" + dataAddPwd[2] + "\n", "Password Manager")
                    if not userConfirm:
                        continue
                self.addPwdToData(dataAddPwd[0], dataAddPwd[1], dataAddPwd[2], dataAddPwd[3])
                break
    
    def addOther(self):
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
                    break
            break