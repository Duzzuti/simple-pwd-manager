import requests
import easygui
import zipfile
import os
import shutil

import settings


def check_for_updates():
    # check for updates on the site https://github.com/Duzzuti/simple-pwd-manager/releases
    # if there is a newer version available, ask the user if they want to download it
    try:
        request = requests.get("https://api.github.com/repos/Duzzuti/simple-pwd-manager/releases/latest")
    except requests.exceptions.RequestException:
        print("Could not check for updates. Please check your internet connection.")
        return
    if request.status_code != 200:
        return
    data = request.json()
    latestVersion = data["tag_name"]
    if settings.isVersionNewer(latestVersion):
        tmp = easygui.ynbox("There is a newer version of the program available. Do you want to download it?\n\nCurrent version: " + settings.version + "\nNew version: " + latestVersion, "Password Manager")
        if tmp:
            download_url = data["zipball_url"]
            try:
                request = requests.get(download_url, allow_redirects=True)
            except requests.exceptions.RequestException:
                easygui.msgbox("Could not download the update. Please check your internet connection.", "Password Manager")
                return
            open("update.zip", "wb").write(request.content)
            # unzip the file
            with zipfile.ZipFile("update.zip", 'r') as zip_ref:
                zip_ref.extractall("update")
            updateDirs = os.listdir("update")
            if len(updateDirs) != 1:
                easygui.msgbox("Some error occurred while updating. There was more than one directory downloaded. Please update manually.", "Password Manager")
                os.remove("update.zip")
                shutil.rmtree("update")
                return
            os.rename("update/"+updateDirs[0], "update/simple-pwd-manager")
            # copy user data to the new directory
            shutil.copytree("userData", "update/simple-pwd-manager/userData")
            shutil.copy("lastUsedFile.txt", "update/simple-pwd-manager/lastUsedFile.txt")
            os.remove("update.zip")

            # remove everything except the update folder
            for item in os.listdir("."):
                if item != "update":
                    try:
                        if os.path.isdir(item):
                            shutil.rmtree(item)
                        else:
                            os.remove(item)
                    except:
                        easygui.msgbox("Some error occurred while updating. Following items could not be removed: " + item, "Password Manager")
                        shutil.rmtree("update")
                        os.remove("update.zip")
                        return

            shutil.copytree("update/simple-pwd-manager", ".", dirs_exist_ok=True)
            shutil.rmtree("update")
            easygui.msgbox("Update successful. The program will now install new dependencies and restart.", "Password Manager")
            # download new dependencies
            pythonNames = ["py", "python", "python3"]
            for name in pythonNames:
                if os.system(name + " -m pip install -r requirements.txt") == 0:
                    break
            else:
                easygui.msgbox("Could not install the required packages, because no python installation found.\nPlease make sure python is accessible with 'py', 'python' or 'python3' and install the dependencies manually with \n'python -m pip install -r requirements.txt'", "Password Manager")
                exit()
            easygui.msgbox("Dependencies installed. New version: " + latestVersion + " is now running.", "Password Manager")
            os.execl("main.py", "main.py")
            exit()