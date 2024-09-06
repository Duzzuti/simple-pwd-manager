import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import easygui
import pandas as pd
import pickle

# string used to verify password
correct_bytes = "kolajlfdalöfdasnifjnasnofjasidfnoiasnfkajsfndjkasdfoasdjfioasdiujf\n".encode()
file = "pEnc.enc"

# Function to generate a key from a password
def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=5000000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Function to decrypt data
def decrypt(data: bytes, key: bytes) -> bytes:
    iv = data[:16]  # The first 16 bytes are the IV
    encrypted_data = data[16:]  # The rest is the encrypted data
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Remove padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data

# Function to decrypt a file
def decrypt_file(input_file: str, password: str):
    with open(input_file, 'rb') as f:
        file_data = f.read()
    
    salt = file_data[:16]  # Extract the salt (first 16 bytes)
    encrypted_data = file_data[16:]  # The rest is encrypted data

    key = generate_key(password, salt)
    try:
        return decrypt(encrypted_data, key)
    except:
        return ""

# Function to encrypt data
def encrypt(data: bytes, key: bytes) -> bytes:
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return iv + encrypted_data

# Function to encrypt a file
def encrypt_pdata(data: bytes, output_file: str, password: str):
    salt = os.urandom(16)  # Generate a random salt
    key = generate_key(password, salt)

    # add correct string at the start of the file
    file_data = correct_bytes
    # add data

    file_data += data

    encrypted_data = encrypt(file_data, key)
    
    with open(output_file, 'wb') as f:
        f.write(salt + encrypted_data)

if __name__ == "__main__":
    password = None
    data = pickle.dumps([pd.DataFrame({"Website": [], "Email": [], "Username": [], "Password": []}), pd.DataFrame({"Name": [], "Info": []})])
    if not os.path.isfile(file):
        user_new_input = easygui.ynbox("No encrypted password file found. Do you want to create a new one?", "Password Manager")
        if user_new_input:
            while True:
                password = easygui.passwordbox("Enter a master password for the file: ", "Password Manager")
                # confirm password
                password_confirm = easygui.passwordbox("Confirm the master password: ", "Password Manager")
                if(password != password_confirm):
                    easygui.msgbox("Passwords do not match. Try again.", "Password Manager")
                else:
                    break
            easygui.msgbox("MAKE SURE TO REMEMBER THE PASSWORD. THERE IS NO WAY TO RECOVER IT.\nIF YOU FORGET THE PASSWORD, ALL DATA IN THE FILE WILL BE LOST.", "Password Manager")
            show_pwd = easygui.ynbox("Show password?\nPLEASE NOTE THAT THIS WILL SHOW SENSITIVE DATA TO THE SCREEN", "Password Manager", ("Yes", "No"))
            if show_pwd:
                easygui.msgbox("Your password is: " + password, "Password Manager")
            user_confirm2 = easygui.ynbox("Make sure to save the password somewhere safe. Please confirm.", "Password Manager")
            while not user_confirm2:
                user_confirm2 = easygui.ynbox("You have to confirm before you can continue.", "Password Manager")
            print("Creating new encrypted password file...")
            open(file, 'w').close()
            encrypt_pdata(data, file, password)
            easygui.msgbox("Welcome to the password manager\nYou can enter your password data in this interface\nThe data will be encrypted with the master password and stored in the file (" + file + ")\nYou should do a backup of the file regularly to avoid losing data\nIf you lose the file, you will lose all data in it", "Password Manager")
        else:
            exit()
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