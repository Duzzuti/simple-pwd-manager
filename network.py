import requests
import easygui
import zipfile
import os
import shutil
import threading

import settings
from settings import language
from basic_UX import ynBox

def check_for_updates(threaded=False):
    def _check_for_updates():
        # check for updates on the site https://github.com/Duzzuti/simple-pwd-manager/releases
        # if there is a newer version available, ask the user if they want to download it
        try:
            request = requests.get("https://api.github.com/repos/Duzzuti/simple-pwd-manager/releases/latest")
        except requests.exceptions.RequestException:
            print(language.ERR_UPDATE_REQUEST_FAILED)
            return
        if request.status_code != 200:
            print(language.ERR_UPDATE_INVALID_STATUS_CODE + str(request.status_code))
            return
        data = request.json()
        latestVersion = data["tag_name"]
        if settings.isVersionNewer(latestVersion):
            tmp = ynBox(language.NEWER_VERSION_AVAILABLE1 + settings.version + language.NEWER_VERSION_AVAILABLE2 + latestVersion, "Password Manager")
            if tmp:
                download_url = data["zipball_url"]
                try:
                    request = requests.get(download_url, allow_redirects=True)
                except requests.exceptions.RequestException:
                    easygui.msgbox(language.ERR_UPDATE_DOWNLOAD_FAILED, "Password Manager")
                    return
                open("update.zip", "wb").write(request.content)
                # unzip the file
                with zipfile.ZipFile("update.zip", 'r') as zip_ref:
                    zip_ref.extractall("update")
                updateDirs = os.listdir("update")
                if len(updateDirs) != 1:
                    easygui.msgbox(language.ERR_UPDATE_MULTIPLE_DIRS, "Password Manager")
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
                            easygui.msgbox(language.ERR_UPDATE_COULD_NOT_REMOVE_ITEM + item, "Password Manager")
                            shutil.rmtree("update")
                            os.remove("update.zip")
                            return

                shutil.copytree("update/simple-pwd-manager", ".", dirs_exist_ok=True)
                shutil.rmtree("update")
                easygui.msgbox(language.UPDATE_SUCCESSFUL_INSTALL_DEPENDENCIES, "Password Manager")
                # download new dependencies
                pythonNames = ["python", "py", "python3"]
                for name in pythonNames:
                    if os.system(name + " -m pip install -r requirements.txt") == 0:
                        break
                else:
                    easygui.msgbox(language.ERR_DEPENDENCIES_DOWNLOAD_FAILED, "Password Manager")
                    exit()
                easygui.msgbox(language.UPDATE_SUCCESSFUL1 + latestVersion + language.UPDATE_SUCCESSFUL2, "Password Manager")
                # shut the main thread down
                os._exit(0)

    if threaded:
        t = threading.Thread(target=_check_for_updates)
        t.start()
        return
    else:
        _check_for_updates()