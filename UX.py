import easygui
import os
import tkinter as tk
from tkinter import Toplevel
from basic_UX import enterBox, ynBox

import structureTools
import encryption
import settings
from settings import language

settingsRoot = None

def createSettingsWindow(root: tk.Tk):
    global settingsRoot
    def onApply():
        updated = False
        if languageVar.get() != language.LANGUAGE:
            updated = True
            settings.setLanguage(languageVar.get())
        if (updateCheckerVar.get() == language.YES) != settings.checkUpdates:
            updated = True
            if updateCheckerVar.get() == language.YES:
                settings.setUpdateChecker(True)
            else:
                settings.setUpdateChecker(False)
        if updated:
            # restart the program
            easygui.msgbox(language.SETTINGS_CHANGE_RESTART)
            os._exit(0)
        settingsRoot.destroy()
        return
        
    if settingsRoot is not None:
        settingsRoot.destroy()
    settingsRoot = Toplevel(root)
    settingsRoot.title(language.SETTINGS)
    settingsRoot.geometry("300x200")
    settingsRoot.resizable(False, False)
    settingsRoot.option_add("*Font", "Helvetica 12")

    # Settings label
    label = tk.Label(settingsRoot, text=language.SETTINGS)
    label.pack(pady=10)

    # Language setting
    languageSetting = tk.Frame(settingsRoot)

    label = tk.Label(languageSetting, text=language.SETTINGS_LANGUAGE)
    label.pack(side="left")

    # Language selection
    languageVar = tk.StringVar(languageSetting)
    languageVar.set(language.LANGUAGE)
    languageMenu = tk.OptionMenu(languageSetting, languageVar, *language.Languages)
    languageMenu.pack(side="right")

    languageSetting.pack(pady=10)

    # Update checker setting
    updateChecker = tk.Frame(settingsRoot)

    label = tk.Label(updateChecker, text=language.SETTINGS_UPDATE_CHECKER)
    label.pack(side="left")

    # Update checker selection
    updateCheckerVar = tk.StringVar(updateChecker)
    updateCheckerVar.set(language.YES if settings.checkUpdates else language.NO)
    updateCheckerMenu = tk.OptionMenu(updateChecker, updateCheckerVar, language.YES, language.NO)
    updateCheckerMenu.pack(side="right")

    updateChecker.pack(pady=10)

    # add Apply and Cancel buttons
    applyButton = tk.Button(settingsRoot, text=language.APPLY, command=onApply)
    applyButton.pack(side="left", padx=20, pady=10)
    cancelButton = tk.Button(settingsRoot, text=language.CANCEL, command=settingsRoot.destroy)
    cancelButton.pack(side="right", padx=20, pady=10)

    settingsRoot.transient(root)  # Keep popup on top of main window
    settingsRoot.focus_set()      # Focus on popup
    settingsRoot.grab_set()       # Make popup modal (blocks interactions with main window)
    settingsRoot.mainloop()

def createPasswordWindow(text: str, title: str, encFiles: list[str], filePath: str) -> tuple[str, str]:
    retCode = "CANCEL"
    result = None
    def onSubmit():
        nonlocal retCode, result
        result = password_entry.get()
        root.destroy()
        retCode, result = "OK", result

    def onChangeFile():
        nonlocal retCode, result
        root.destroy()
        newPath = chooseEncFile(encFiles, preselectFile=filePath)
        if len(encFiles) == 1:
            easygui.msgbox(language.ERR_NO_OTHER_USER_DATA_FILES_FOUND + structureTools.userDataDir + "/)", "Password Manager")
        retCode, result = "CHANGE", newPath
    
    def onNewFile():
        nonlocal retCode, result
        root.destroy()
        retCode, result = "NEW", None
    
    def onSetting():
        createSettingsWindow(root)
    
    root = tk.Tk()
    root.title(title)
    # root.geometry("386x127")
    # set window to screen position 300 x 200
    root.geometry("+300+200")
    root.resizable(True, True)
    root.option_add("*Font", "Helvetica 12")

    # Password entry label, make it auto adjust to text
    label = tk.Label(root, text=text)
    label.pack(pady=10)
    # adjust on resize
    root.bind("<Configure>", lambda e: label.config(wraplength=root.winfo_width()-20))

    # Password entry field with full width
    password_entry = tk.Entry(root, show="*", width=40)
    password_entry.pack(pady=5, padx=10)
    password_entry.focus_force()

    # Submit Button
    submitButton = tk.Button(root, text=language.LOGIN, command=onSubmit)
    submitButton.pack(side="left", padx=20, pady=10)
    # make submit button activate on enter
    root.bind("<Return>", lambda e: submitButton.invoke())

    # Cancel Button
    tmp = tk.PhotoImage(file="assets/settings.png").subsample(22)
    cancelButton = tk.Button(root, text=" "+language.SETTINGS, command=onSetting, image=tmp, compound=tk.LEFT)
    cancelButton.pack(side="left", padx=20, pady=10)
    # make cancel button activate on escape
    root.bind("<Escape>", lambda e: cancelButton.invoke())

    # Change File Button
    changeFileButton = tk.Button(root, text=language.CHANGE_FILE, command=onChangeFile)
    changeFileButton.pack(side="right", padx=20, pady=10)

    # New File Button
    newFileButton = tk.Button(root, text=language.NEW_FILE, command=onNewFile)
    newFileButton.pack(side="right", padx=20, pady=10)

    root.resizable(False, False)
    root.mainloop()
    return (retCode, result)


# let the user create a new file and returns (filePath, password)
def newFileHandler(noFileFound=False) -> tuple[str, str]:
    while True:
        if noFileFound:
            msg = language.CREATE_NEW_FILE_NO_FILE_FOUND
        else:
            msg = language.CREATE_NEW_FILE_ENTER_NEW_FILE_NAME
        newFileName = enterBox(msg, "Password Manager", structureTools.defaultEncFileWithoutExt)
        if newFileName is None:
            exit()
        if structureTools.verifyFileName(newFileName):
            break
    while True:
        password = easygui.passwordbox(language.CREATE_NEW_FILE_ENTER_PASSWORD, "Password Manager")
        if password is None:
            exit()
        if not password:
            easygui.msgbox(language.ERR_NON_EMPTY_PASSWORD_REQUIRED, "Password Manager")
            continue
        # confirm password
        passwordConfirm = easygui.passwordbox(language.CREATE_NEW_FILE_CONFIRM_PASSWORD, "Password Manager")
        if passwordConfirm is None:
            exit()
        if(password == passwordConfirm):
            break
        easygui.msgbox(language.ERR_PASSWORDS_DO_NOT_MATCH, "Password Manager")

    tmpUserInp = easygui.msgbox(language.CREATE_NEW_FILE_REMEMBER_DISCLAIMER, "Password Manager")
    if tmpUserInp is None:
        exit()
    showPwd = ynBox(language.CREATE_NEW_FILE_SHOW_PASSWORD_PROMPT, "Password Manager")
    if showPwd is None:
        exit()
    if showPwd:
        easygui.msgbox(language.YOUR_PASSWORD_IS + password, "Password Manager")
    userPwdSafeConfirm = ynBox(language.CREATE_NEW_FILE_CONFIRM_PASSWORD_SAVED, "Password Manager")
    while not userPwdSafeConfirm:
        if userPwdSafeConfirm is None:
            exit()
        userPwdSafeConfirm = ynBox(language.CREATE_NEW_FILE_CONFIRM_PASSWORD_SAVED_AGAIN, "Password Manager")
    print(language.CREATE_NEW_FILE_CREATING)
    structureTools.createEncryptedFile(newFileName, password)
    easygui.msgbox(language.CREATE_NEW_FILE_WELCOME1 + newFileName + language.CREATE_NEW_FILE_WELCOME2, "Password Manager")
    return (os.path.join(structureTools.userDataDir, newFileName + settings.extension), password)

def chooseEncFile(encFiles: list[str], isFullPath = True, preselectFile: str = None) -> str:
    preselectIndex = 0
    if len(encFiles) == 1:
        return encFiles[0]
    if preselectFile is not None:
        if preselectFile not in encFiles:
            print(language.ERR_PRESELECTED_FILE_NOT_FOUND1 + preselectFile + language.ERR_PRESELECTED_FILE_NOT_FOUND2)
            exit()
        # get index of preselectFile
        preselectIndex = encFiles.index(preselectFile)
    fileName = easygui.choicebox(language.CHOOSE_FILE, "Password Manager", encFiles, preselectIndex)
    if fileName is None:
        exit()
    if isFullPath:
        return fileName
    return os.path.join(structureTools.userDataDir, fileName + settings.extension)

def getPassword(filePath: str, encFiles: list[str]) -> tuple[str, str, bytes]:
    while True:
        retCode, result = createPasswordWindow(language.ENTER_MASTER_PASSWORD + filePath + "): ", "Password Manager", encFiles, filePath)
        if retCode == "CANCEL":
            exit()
        elif retCode == "CHANGE":
            filePath = result
        elif retCode == "NEW":
            newFilePath, newPassword = newFileHandler()
            return (newFilePath, newPassword, None)
        elif retCode == "OK":
            password = result
            if password is None:
                exit()
            dataBytes = encryption.decrypt_file(filePath, password)
            while(not dataBytes):
                password = easygui.passwordbox(language.ERR_WRONG_MASTER_PASSWORD1 + filePath + language.ERR_WRONG_MASTER_PASSWORD2, "Password Manager")
                if password is None:
                    exit()
                dataBytes = encryption.decrypt_file(filePath, password)
            structureTools.saveLastUsedFile(os.path.basename(filePath)[:-len(settings.extension)])
            return (filePath, password, dataBytes)
        else:
            print(language.ERR_INVALID_RETURN_CODE + retCode)
            exit()
