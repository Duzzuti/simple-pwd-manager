class Language():
    Languages = ["English", "Deutsch"]
    LANGUAGE = None

    # ADDONS
    ADD_LOGIN = None
    ADD_OTHER = None
    APPLY = None
    CANCEL = None
    CHANGE_FILE = None
    CHANGE_INFORMATION = None
    DELETE = None
    DELETE_CHANGE_LOGIN = None
    EXIT = None
    NEW_FILE = None
    NO = None
    REQUIRED = None
    SHOW_LOGINS = None
    SHOW_OTHER = None
    SKIP = None
    YES = None

    # NAMES
    EMAIL = None
    INFO_CONTENT = None
    INFO_TITLE = None
    LOGIN = None
    PASSWORD = None
    SETTINGS = None
    SETTINGS_LANGUAGE = None
    SETTINGS_UPDATE_CHECKER = None
    USERNAME = None
    WEBSITE_APP = None

    # INFO
    ADD_INFO_TITLE = None
    CHOOSE_ACTION = None
    CHOOSE_ACTION_FOR = None
    CHOOSE_FILE = None
    CHOOSE_WEBSITE_TO_CHANGE_DELETE = None
    CREATE_NEW_FILE_CONFIRM_PASSWORD = None
    CREATE_NEW_FILE_CONFIRM_PASSWORD_SAVED = None
    CREATE_NEW_FILE_CONFIRM_PASSWORD_SAVED_AGAIN = None
    CREATE_NEW_FILE_CREATING = None
    CREATE_NEW_FILE_ENTER_NEW_FILE_NAME = None
    CREATE_NEW_FILE_ENTER_PASSWORD = None
    CREATE_NEW_FILE_NO_FILE_FOUND = None
    CREATE_NEW_FILE_REMEMBER_DISCLAIMER = None
    CREATE_NEW_FILE_SHOW_PASSWORD_PROMPT = None
    CREATE_NEW_FILE_WELCOME1 = None
    CREATE_NEW_FILE_WELCOME2 = None
    CURRENT_LOGINS_FOR = None
    DEPENDENCIES_INSTALLED = None
    ENTER_FOLLOWING = None
    ENTER_MASTER_PASSWORD = None
    ENTER_TO_EXIT = None
    ENTER_TO_CLEAR = None
    INFO_CONTENT_REQUIRED = None
    INFO_TITLE_REQUIRED = None
    NEW_INFORMATION = None
    NEWER_VERSION_AVAILABLE1 = None
    NEWER_VERSION_AVAILABLE2 = None
    NEWER_VERSION_AVAILABLE3 = None
    NO_LOGINS_FOUND = None
    NO_OTHER_INFO_FOUND = None
    PASSWORD_ENTRY_ALREADY_EXISTS_MESSAGE = None
    RESTART_ENTER_TO_EXIT = None
    SETTINGS_CHANGE_RESTART = None
    STORE_INFORMATION_FOR = None
    UPDATE_SUCCESSFUL_INSTALL_DEPENDENCIES = None
    UPDATE_SUCCESSFUL1 = None
    UPDATE_SUCCESSFUL2 = None
    YOUR_PASSWORD_IS = None
    WEBSITE_PASSWORD_REQUIRED = None

    # ERRORS
    ERR_DEPENDENCIES_DOWNLOAD_FAILED = None
    ERR_ENTER_TO_EXIT = None
    ERR_FILE_CORRUPTED_FORMAT = None
    ERR_FILE_COULD_NOT_BE_DECRYPTED = None
    ERR_FILE_EMPTY = None
    ERR_FILE_FORMAT_INVALID_PARAMETERS = None
    ERR_FILE_FORMAT_INVALID_SALT = None
    ERR_FILE_NAME_ALREADY_EXISTS1 = None
    ERR_FILE_NAME_ALREADY_EXISTS2 = None
    ERR_FILE_NAME_CANNOT_BE_EMPTY = None
    ERR_FILE_NAME_CONTAINS_INVALID_CHARACTERS1 = None
    ERR_FILE_NAME_CONTAINS_INVALID_CHARACTERS2 = None
    ERR_INVALID_RETURN_CODE = None
    ERR_KEY_GENERATION = None
    ERR_LAST_USED_FILE_NOT_FOUND1 = None
    ERR_LAST_USED_FILE_NOT_FOUND2 = None
    ERR_META_REQUIRED = None
    ERR_MISSING_DEPENDENCIES = None
    ERR_NO_OTHER_USER_DATA_FILES_FOUND = None
    ERR_NON_EMPTY_PASSWORD_REQUIRED = None
    ERR_PASSWORDS_DO_NOT_MATCH = None
    ERR_PRESELECTED_FILE_NOT_FOUND1 = None
    ERR_PRESELECTED_FILE_NOT_FOUND2 = None
    ERR_PROGRAM_OUTDATED1 = None
    ERR_PROGRAM_OUTDATED2 = None
    ERR_SETTINGS_OUT_OF_BOUNDS = None
    ERR_UPDATE_CHECKER_FILE_CORRUPTED = None
    ERR_UPDATE_CHECKER_FILE_NOT_FOUND = None
    ERR_UPDATE_COULD_NOT_REMOVE_ITEM = None
    ERR_UPDATE_DOWNLOAD_FAILED = None
    ERR_UPDATE_INVALID_STATUS_CODE = None
    ERR_UPDATE_MULTIPLE_DIRS = None
    ERR_UPDATE_REQUEST_FAILED = None
    ERR_USERDATA_CONTAINS_INVALID_FILES1 = None
    ERR_USERDATA_CONTAINS_INVALID_FILES2 = None
    ERR_WHILE_DECRYPTING_FILE = None
    ERR_WRONG_MASTER_PASSWORD1 = None
    ERR_WRONG_MASTER_PASSWORD2 = None

class English(Language):
    LANGUAGE = "English"

    # ADDONS
    ADD_LOGIN = "Add login"
    ADD_OTHER = "Add other"
    APPLY = "Apply"
    CANCEL = "Cancel"
    CHANGE_FILE = "Change File"
    CHANGE_INFORMATION = "Change information"
    DELETE = "Delete"
    DELETE_CHANGE_LOGIN = "Delete/Change login"
    EXIT = "Exit"
    NEW_FILE = "New File"
    NO = "No"
    REQUIRED = "(required)"
    SHOW_LOGINS = "Show logins"
    SHOW_OTHER = "Show other"
    SKIP = "Skip"
    YES = "Yes"

    # NAMES
    EMAIL = "Email"
    INFO_CONTENT = "Content"
    INFO_TITLE = "Title"
    LOGIN = "Login"
    PASSWORD = "Password"
    SETTINGS = "Settings"
    SETTINGS_LANGUAGE = "Language: "
    SETTINGS_UPDATE_CHECKER = "Update checks: "
    USERNAME = "Username"
    WEBSITE_APP = "Website/App"

    # INFO
    ADD_INFO_TITLE = "Enter a title for the information you want to add. This is only for your reference."
    CHOOSE_ACTION = "Choose an action: "
    CHOOSE_ACTION_FOR = "Choose an action for "
    CHOOSE_FILE = "Choose a file to open: "
    CHOOSE_WEBSITE_TO_CHANGE_DELETE = "Choose the websites/apps to delete or change the information for: "
    CREATE_NEW_FILE_CONFIRM_PASSWORD = "Confirm the master password: "
    CREATE_NEW_FILE_CONFIRM_PASSWORD_SAVED = "Make sure to save the password somewhere safe. Please confirm."
    CREATE_NEW_FILE_CONFIRM_PASSWORD_SAVED_AGAIN = "You have to confirm before you can continue. Please make sure your password is backed up somewhere."
    CREATE_NEW_FILE_CREATING = "Creating new encrypted password file..."
    CREATE_NEW_FILE_ENTER_NEW_FILE_NAME = "Enter new file name:"
    CREATE_NEW_FILE_ENTER_PASSWORD = "Enter a master password for the file: "
    CREATE_NEW_FILE_NO_FILE_FOUND = "No encrypted password file found. Creating a new file...\nEnter file name:"
    CREATE_NEW_FILE_REMEMBER_DISCLAIMER = "MAKE SURE TO REMEMBER THE PASSWORD. THERE IS NO WAY TO RECOVER IT.\nIF YOU FORGET THE PASSWORD, ALL DATA IN THE FILE WILL BE LOST."
    CREATE_NEW_FILE_SHOW_PASSWORD_PROMPT = "Show password?\nPLEASE NOTE THAT THIS WILL SHOW SENSITIVE DATA TO THE SCREEN"
    CREATE_NEW_FILE_WELCOME1 = "Welcome to the password manager\nYou can enter your login data in this interface\nThe data will be encrypted with the master password and stored in the file ("
    CREATE_NEW_FILE_WELCOME2 = ")\nYou should do a backup of the file regularly to avoid losing data\nIf you lose the file, you will lose all data in it"
    CURRENT_LOGINS_FOR = "Current logins for "
    DEPENDENCIES_INSTALLED = "Dependencies installed. You are ready to run the program."
    ENTER_FOLLOWING = "Enter the following information: "
    ENTER_MASTER_PASSWORD = "Enter the master password for the file ("
    ENTER_TO_EXIT = "Press enter to exit..."
    ENTER_TO_CLEAR = "Press enter to clear..."
    INFO_CONTENT_REQUIRED = "Please enter the information you want to save. Cannot be empty."
    INFO_TITLE_REQUIRED = "A title is required."
    NEW_INFORMATION = "New information"
    NEWER_VERSION_AVAILABLE1 = "There is a newer version of the program available. Do you want to download and install it?\n\nCurrent version: "
    NEWER_VERSION_AVAILABLE2 = "\nNew version: "
    NEWER_VERSION_AVAILABLE3 = "\n\nYou can disable the automatic update check in the settings."
    NO_LOGINS_FOUND = "No logins found."
    NO_OTHER_INFO_FOUND = "No other information found."
    PASSWORD_ENTRY_ALREADY_EXISTS_MESSAGE = "An entry for this website/app already exists. Do you want to add the information as an other login? (No does NOT safe the new information). \nIf you want to change old information (e.g. a single password) please use the 'Change password' section of the main menu.\n\n"
    RESTART_ENTER_TO_EXIT = "Please restart the program. Press enter to exit..."
    SETTINGS_CHANGE_RESTART = "Please restart the program to apply the changes."
    STORE_INFORMATION_FOR = "Store information for "
    UPDATE_SUCCESSFUL_INSTALL_DEPENDENCIES = "Update successful. The program will now install new dependencies."
    UPDATE_SUCCESSFUL1 = "Dependencies up to date. New version: "
    UPDATE_SUCCESSFUL2 = " is now installed.\nPlease restart the program to use the new version.\nNOTE THAT UNSAVED CHANGES WILL BE LOST"
    YOUR_PASSWORD_IS = "Your password is: "
    WEBSITE_PASSWORD_REQUIRED = "A website/app and a password is required."

    # ERRORS
    ERR_DEPENDENCIES_DOWNLOAD_FAILED = "Could not install the required packages, because no python installation found.\nPlease make sure python is accessible with 'py', 'python' or 'python3' or install the dependencies manually with \n'python -m pip install -r requirements.txt'"
    ERR_ENTER_TO_EXIT = "An error occurred. Press enter to exit..."
    ERR_FILE_CORRUPTED_FORMAT = "The file is corrupted. The format is not as expected."
    ERR_FILE_COULD_NOT_BE_DECRYPTED = "The file could not be decrypted. Please try again."
    ERR_FILE_EMPTY = "File is empty."
    ERR_FILE_FORMAT_INVALID_PARAMETERS = "Invalid file format: Not enough data for n, r and p arguments."
    ERR_FILE_FORMAT_INVALID_SALT = "Invalid file format: Salt length is greater than remaining file size."
    ERR_FILE_NAME_ALREADY_EXISTS1 = "A file with the name '"
    ERR_FILE_NAME_ALREADY_EXISTS2 = "' already exists. Please choose another name."
    ERR_FILE_NAME_CANNOT_BE_EMPTY = "The file name cannot be empty."
    ERR_FILE_NAME_CONTAINS_INVALID_CHARACTERS1 = "The file name contains invalid characters ('"
    ERR_FILE_NAME_CONTAINS_INVALID_CHARACTERS2 = "'). Only letters, numbers and underscores are allowed."
    ERR_INVALID_RETURN_CODE = "Error in getPassword: Invalid return code: "
    ERR_KEY_GENERATION = "Error while generating keys, probably due to invalid settings or corrupted data."
    ERR_LAST_USED_FILE_NOT_FOUND1 = "The last used file ("
    ERR_LAST_USED_FILE_NOT_FOUND2 = ") was not found. Copy the file back to the location or choose an other file to open."
    ERR_META_REQUIRED = "Meta data is required for this action."
    ERR_MISSING_DEPENDENCIES = "There are missing dependencies. Installing them now..."
    ERR_NO_OTHER_USER_DATA_FILES_FOUND = "No other files found in user data directory ("
    ERR_NON_EMPTY_PASSWORD_REQUIRED = "A non empty password is required."
    ERR_PASSWORDS_DO_NOT_MATCH = "Passwords do not match. Try again."
    ERR_PRESELECTED_FILE_NOT_FOUND1 = "Error in chooseEncFile: preselectFile ("
    ERR_PRESELECTED_FILE_NOT_FOUND2 = ") not in encFiles"
    ERR_PROGRAM_OUTDATED1 = "The file was created with a newer version of the program. Please update the program to open the file. (File version: "
    ERR_PROGRAM_OUTDATED2 = ", Program version: "
    ERR_SETTINGS_OUT_OF_BOUNDS = "Some settings were set out of bounds."
    ERR_UPDATE_CHECKER_FILE_CORRUPTED = "The settings file for the update checker is corrupted. Default values are used (automatic update check)."
    ERR_UPDATE_CHECKER_FILE_NOT_FOUND = "The settings file for the update checker was not found. Default values are used (automatic update check)."
    ERR_UPDATE_COULD_NOT_REMOVE_ITEM = "Some error occurred while updating. Following items could not be removed: "
    ERR_UPDATE_DOWNLOAD_FAILED = "Could not download the update. Please check your internet connection."
    ERR_UPDATE_INVALID_STATUS_CODE = "Could not check for updates. Got status code: "
    ERR_UPDATE_MULTIPLE_DIRS = "Some error occurred while updating. There was more than one directory downloaded. Please update manually."
    ERR_UPDATE_REQUEST_FAILED = "Could not check for updates. Please check your internet connection."
    ERR_USERDATA_CONTAINS_INVALID_FILES1 = "The userData directory contains files or directories that should not be there (namely: "
    ERR_USERDATA_CONTAINS_INVALID_FILES2 = "). Please remove them."
    ERR_WHILE_DECRYPTING_FILE = "Error while decrypting file: "
    ERR_WRONG_MASTER_PASSWORD1 = "Wrong password for file ("
    ERR_WRONG_MASTER_PASSWORD2 = "). Please try again."
    
class German(Language):
    LANGUAGE = "Deutsch"
    # ADDONS
    ADD_LOGIN = "Login hinzufügen"
    ADD_OTHER = "Sonstiges hinzufügen"
    APPLY = "Anwenden"
    CANCEL = "Abbrechen"
    CHANGE_FILE = "Datei ändern"
    CHANGE_INFORMATION = "Informationen ändern"
    DELETE = "Löschen"
    DELETE_CHANGE_LOGIN = "Anmeldedaten löschen/ändern"
    EXIT = "Beenden"
    NEW_FILE = "Neue Datei"
    NO = "Nein"
    REQUIRED = "(erforderlich)"
    SHOW_LOGINS = "Anmeldedaten anzeigen"
    SHOW_OTHER = "Sonstiges anzeigen"
    SKIP = "Überspringen"
    YES = "Ja"

    # NAMES
    EMAIL = "Email"
    INFO_CONTENT = "Inhalt"
    INFO_TITLE = "Titel"
    LOGIN = "Anmelden"
    PASSWORD = "Passwort"
    SETTINGS = "Einstellungen"
    SETTINGS_LANGUAGE = "Sprache: "
    SETTINGS_UPDATE_CHECKER = "Nach Updates suchen: "
    USERNAME = "Benutzername"
    WEBSITE_APP = "Webseite/App"

    # INFO
    ADD_INFO_TITLE = "Vergeben Sie einen Titel für die Informationen, die Sie hinzufügen möchten."
    CHOOSE_ACTION = "Wählen Sie eine Aktion: "
    CHOOSE_ACTION_FOR = "Wählen Sie eine Aktion für "
    CHOOSE_FILE = "Wählen Sie eine Datei zum Öffnen: "
    CHOOSE_WEBSITE_TO_CHANGE_DELETE = "Wählen Sie die Webseiten/Apps, für die Sie die Informationen löschen oder ändern möchten: "
    CREATE_NEW_FILE_CONFIRM_PASSWORD = "Wiederholen Sie das Passwort: "
    CREATE_NEW_FILE_CONFIRM_PASSWORD_SAVED = "Stellen Sie sicher, dass Sie das Passwort an einem sicheren Ort speichern. Bitte bestätigen."
    CREATE_NEW_FILE_CONFIRM_PASSWORD_SAVED_AGAIN = "Sie müssen bestätigen, bevor Sie fortfahren können. Bitte stellen Sie sicher, dass Ihr Passwort an einem sicheren Ort gespeichert ist."
    CREATE_NEW_FILE_CREATING = "Erstelle neue verschlüsselte Datei..."
    CREATE_NEW_FILE_ENTER_NEW_FILE_NAME = "Vergeben Sie einen Dateinamen:"
    CREATE_NEW_FILE_ENTER_PASSWORD = "Vergeben Sie ein Master-Passwort für die Datei: "
    CREATE_NEW_FILE_NO_FILE_FOUND = "Keine Dateien gefunden. Erstelle eine neue Datei...\nDateinamen eingeben:"
    CREATE_NEW_FILE_REMEMBER_DISCLAIMER = "STELLEN SIE SICHER, DASS SIE DAS PASSWORT SICHERN. ES GIBT KEINE MÖGLICHKEIT, ES WIEDERHERZUSTELLEN.\nWENN SIE DAS PASSWORT VERGESSEN, GEHEN ALLE DATEN IN DER DATEI VERLOREN."
    CREATE_NEW_FILE_SHOW_PASSWORD_PROMPT = "Passwort anzeigen?\nBITTE BEACHTEN SIE, DASS DIES SENSIBLE DATEN AUF DEM BILDSCHIRM ANZEIGT"
    CREATE_NEW_FILE_WELCOME1 = "Willkommen beim Passwort-Manager\nSie können Ihre Anmeldedaten in dieser Oberfläche eingeben\nDie Daten werden mit dem Master-Passwort verschlüsselt und in der Datei gespeichert ("
    CREATE_NEW_FILE_WELCOME2 = ")\nSie sollten regelmäßig ein Backup der Datei erstellen, um Datenverlust zu vermeiden\nWenn Sie die Datei verlieren, verlieren Sie alle Daten darin"
    CURRENT_LOGINS_FOR = "Aktuelle Anmeldedaten für "
    DEPENDENCIES_INSTALLED = "Zugehörige Pakete wurden installiert. Das Programm ist einsatzbereit."
    ENTER_FOLLOWING = "Geben Sie die folgenden Informationen ein: "
    ENTER_MASTER_PASSWORD = "Geben Sie das Master-Passwort für die Datei ein ("
    ENTER_TO_EXIT = "Drücken Sie Enter, um das Programm zu beenden..."
    ENTER_TO_CLEAR = "Drücken Sie Enter, um die Daten vom Bildschirm zu löschen..."
    INFO_CONTENT_REQUIRED = "Geben Sie erst die Informationen ein, die Sie speichern wollen."
    INFO_TITLE_REQUIRED = "Ein Titel ist erforderlich."
    NEW_INFORMATION = "Neue Information"
    NEWER_VERSION_AVAILABLE1 = "Es ist eine neuere Version des Programms verfügbar. Möchten Sie diese herunterladen und installieren?\n\nAktuelle Version: "
    NEWER_VERSION_AVAILABLE2 = "\nNeue Version: "
    NEWER_VERSION_AVAILABLE3 = "\n\nSie können die automatische Suche nach Updates in den Einstellungen deaktivieren."
    NO_LOGINS_FOUND = "Keine Anmeldedaten gefunden."
    NO_OTHER_INFO_FOUND = "Keine sonstigen Informationen gefunden."
    PASSWORD_ENTRY_ALREADY_EXISTS_MESSAGE = "Ein Eintrag für diese Webseite/App existiert bereits. Möchten Sie die Informationen als weitere Anmeldung hinzufügen? (Nein speichert die neuen Informationen NICHT). \nWenn Sie alte Informationen ändern möchten (z.B. ein einzelnes Passwort), verwenden Sie bitte den Abschnitt 'Anmeldedaten ändern' im Hauptmenü.\n\n"
    RESTART_ENTER_TO_EXIT = "Bitte starten Sie das Programm neu. Drücken Sie Enter, um das Programm zu beenden..."
    SETTINGS_CHANGE_RESTART = "Bitte starten Sie das Programm neu, um die Änderungen zu übernehmen."
    STORE_INFORMATION_FOR = "Informationen speichern für "
    UPDATE_SUCCESSFUL_INSTALL_DEPENDENCIES = "Update erfolgreich. Das Programm wird nun neue zugehörige Pakete installieren."
    UPDATE_SUCCESSFUL1 = "Alle Pakete auf dem neuesten Stand. Neue Version: "
    UPDATE_SUCCESSFUL2 = " ist jetzt installiert.\nBitte starten Sie das Programm neu, um die neue Version zu verwenden.\nNICHT GESPEICHERTE ÄNDERUNGEN GEHEN VERLOREN"
    YOUR_PASSWORD_IS = "Ihr Passwort ist: "
    WEBSITE_PASSWORD_REQUIRED = "Eine Webseite/App und ein Passwort sind erforderlich."

    # ERRORS
    ERR_DEPENDENCIES_DOWNLOAD_FAILED = "Die erforderlichen Pakete konnten nicht installiert werden, da keine Python-Installation gefunden wurde.\nBitte stellen Sie sicher, dass Python mit 'py', 'python' oder 'python3' über ein Terminal erreichbar ist, oder installieren Sie die Pakete manuell mit \n'python -m pip install -r requirements.txt'"
    ERR_ENTER_TO_EXIT = "Ein Fehler ist aufgetreten. Drücken Sie Enter, um das Programm zu beenden..."
    ERR_FILE_CORRUPTED_FORMAT = "Die Datei ist beschädigt. Das Format ist nicht wie erwartet."
    ERR_FILE_COULD_NOT_BE_DECRYPTED = "Die Datei konnte nicht entschlüsselt werden. Bitte versuchen Sie es erneut."
    ERR_FILE_EMPTY = "Die Datei ist leer."
    ERR_FILE_FORMAT_INVALID_PARAMETERS = "Ungültiges Dateiformat: Nicht genügend Daten für die n-, r- und p-Argumente."
    ERR_FILE_FORMAT_INVALID_SALT = "Ungültiges Dateiformat: Die Länge des Salzes ist größer als die verbleibende Dateigröße."
    ERR_FILE_NAME_ALREADY_EXISTS1 = "Eine Datei mit dem Namen '"
    ERR_FILE_NAME_ALREADY_EXISTS2 = "' existiert bereits. Bitte wählen Sie einen anderen Namen."
    ERR_FILE_NAME_CANNOT_BE_EMPTY = "Der Dateiname darf nicht leer sein."
    ERR_FILE_NAME_CONTAINS_INVALID_CHARACTERS1 = "Der Dateiname enthält ungültige Zeichen ('"
    ERR_FILE_NAME_CONTAINS_INVALID_CHARACTERS2 = "'). Es sind nur Buchstaben, Zahlen und Unterstriche erlaubt."
    ERR_INVALID_RETURN_CODE = "Fehler in getPassword: Ungültiger Rückgabecode: "
    ERR_KEY_GENERATION = "Fehler bei der Schlüsselerzeugung, wahrscheinlich aufgrund ungültiger Einstellungen oder beschädigter Daten."
    ERR_LAST_USED_FILE_NOT_FOUND1 = "Die zuletzt verwendete Datei ("
    ERR_LAST_USED_FILE_NOT_FOUND2 = ") wurde nicht gefunden. Kopieren Sie die Datei zurück an den Speicherort oder wählen Sie eine andere Datei zum Öffnen."
    ERR_META_REQUIRED = "Meta-Daten sind für diese Aktion erforderlich."
    ERR_MISSING_DEPENDENCIES = "Es fehlen zugehörige Pakete. Diese werden jetzt installiert..."
    ERR_NO_OTHER_USER_DATA_FILES_FOUND = "Keine weiteren Dateien im Benutzerverzeichnis gefunden ("
    ERR_NON_EMPTY_PASSWORD_REQUIRED = "Passwort darf nicht leer sein."
    ERR_PASSWORDS_DO_NOT_MATCH = "Passwörter stimmen nicht überein. Versuchen Sie es erneut."
    ERR_PRESELECTED_FILE_NOT_FOUND1 = "Fehler in chooseEncFile: preselectFile ("
    ERR_PRESELECTED_FILE_NOT_FOUND2 = ") nicht in encFiles"
    ERR_PROGRAM_OUTDATED1 = "Die Datei wurde mit einer neueren Version des Programms erstellt. Bitte aktualisieren Sie das Programm, um die Datei zu öffnen. (Dateiversion: "
    ERR_PROGRAM_OUTDATED2 = ", Programmversion: "
    ERR_SETTINGS_OUT_OF_BOUNDS = "Einige Einstellungen wurden außerhalb der zulässigen Grenzen gesetzt."
    ERR_UPDATE_CHECKER_FILE_CORRUPTED = "Die Einstellungsdatei für die Suche nach Updates ist beschädigt. Standardwerte werden verwendet (automatische Suche nach Updates)."
    ERR_UPDATE_CHECKER_FILE_NOT_FOUND = "Die Einstellungsdatei für die Suche nach Updates wurde nicht gefunden. Standardwerte werden verwendet (automatische Suche nach Updates)."
    ERR_UPDATE_COULD_NOT_REMOVE_ITEM = "Ein Fehler ist beim Aktualisieren aufgetreten. Folgende Elemente konnten nicht entfernt werden: "
    ERR_UPDATE_DOWNLOAD_FAILED = "Das Update konnte nicht heruntergeladen werden. Bitte überprüfen Sie Ihre Internetverbindung."
    ERR_UPDATE_INVALID_STATUS_CODE = "Ein Fehler ist beim Suchen nach Updates aufgetreten. Statuscode: "
    ERR_UPDATE_MULTIPLE_DIRS = "Ein Fehler ist beim Aktualisieren aufgetreten. Es wurden mehrere Verzeichnisse heruntergeladen. Bitte aktualisieren Sie manuell."
    ERR_UPDATE_REQUEST_FAILED = "Konnte nicht nach Updates suchen. Bitte überprüfen Sie Ihre Internetverbindung."
    ERR_USERDATA_CONTAINS_INVALID_FILES1 = "Das Benutzerverzeichnis enthält Dateien oder Verzeichnisse, die nicht dort sein sollten (nämlich: "
    ERR_USERDATA_CONTAINS_INVALID_FILES2 = "). Bitte entfernen Sie diese."
    ERR_WHILE_DECRYPTING_FILE = "Fehler beim Entschlüsseln der Datei: "
    ERR_WRONG_MASTER_PASSWORD1 = "Falsches Passwort für Datei ("
    ERR_WRONG_MASTER_PASSWORD2 = "). Bitte versuchen Sie es erneut."

def loadLanguage() -> Language:
    try:
        lang = open("language.txt", "r").read()
    except:
        print("Language file not found. Setting to English.")
        open("language.txt", "w").write("English")
        return English()
    if lang == "English":
        return English()
    elif lang == "Deutsch":
        return German()
    else:
        print("Language (", lang, ") not found. Setting to English.")
        open("language.txt", "w").write("English")
        return English()