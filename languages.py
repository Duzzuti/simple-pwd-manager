class Language():
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
    REQUIRED = None
    SHOW_LOGINS = None
    SHOW_OTHER = None
    SKIP = None

    # NAMES
    EMAIL = None
    INFO_CONTENT = None
    INFO_TITLE = None
    LOGIN = None
    PASSWORD = None
    SETTINGS = None
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
    NO_LOGINS_FOUND = None
    NO_OTHER_INFO_FOUND = None
    PASSWORD_ENTRY_ALREADY_EXISTS_MESSAGE = None
    RESTART_ENTER_TO_EXIT = None
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
    REQUIRED = "(required)"
    SHOW_LOGINS = "Show logins"
    SHOW_OTHER = "Show other"
    SKIP = "Skip"

    # NAMES
    EMAIL = "Email"
    INFO_CONTENT = "Content"
    INFO_TITLE = "Title"
    LOGIN = "Login"
    PASSWORD = "Password"
    SETTINGS = "Settings"
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
    DEPENDENCIES_INSTALLED = "Dependencies installed. You can now run the program."
    ENTER_FOLLOWING = "Enter the following information: "
    ENTER_MASTER_PASSWORD = "Enter the master password for the file ("
    ENTER_TO_EXIT = "Press enter to exit..."
    ENTER_TO_CLEAR = "Press Enter to clear..."
    INFO_CONTENT_REQUIRED = "The information is required."
    INFO_TITLE_REQUIRED = "A title is required."
    NEW_INFORMATION = "New information"
    NEWER_VERSION_AVAILABLE1 = "There is a newer version of the program available. Do you want to download and install it?\n\nCurrent version: "
    NEWER_VERSION_AVAILABLE2 = "\nNew version: "
    NO_LOGINS_FOUND = "No logins found."
    NO_OTHER_INFO_FOUND = "No other information found."
    PASSWORD_ENTRY_ALREADY_EXISTS_MESSAGE = "An entry for this website/app already exists. Do you want to add the information as an other login? (No does NOT safe the new information). \nIf you want to change old information (e.g. a single password) please use the 'Change password' section of the main menu.\n\n"
    RESTART_ENTER_TO_EXIT = "Please restart the program. Press enter to exit..."
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
    

def loadLanguage() -> Language:
    return English