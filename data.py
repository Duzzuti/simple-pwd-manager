import pickle
import pandas as pd
import easygui
import os

class Data:
    def __init__(self):
        self.pwd = pd.DataFrame({"Website": [], "Email": [], "Username": [], "Password": []})
        self.other = pd.DataFrame({"Name": [], "Info": []})
        self.byteData = pickle.dumps([self.pwd, self.other])
    
    def getByteData(self) -> bytes:
        return self.byteData

    def addPwdToData(self, website: str, email: str, username: str, password: str):
        self.pwd = pd.concat([self.pwd, pd.DataFrame({"Website": [website], "Email": [email], "Username": [username], "Password": [password]})], ignore_index=True)
        self.byteData = pickle.dumps([self.pwd, self.other])

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