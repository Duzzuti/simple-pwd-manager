import os

from settings import language

def installDependencies():
    try:
        pythonNames = ["python", "py", "python3"]
        for name in pythonNames:
            # download new dependencies
            if os.system(name + " -m pip install -r requirements.txt") == 0:
                break
        else:
            print(language.ERR_DEPENDENCIES_DOWNLOAD_FAILED)
            input(language.ENTER_TO_EXIT)
            return False
        print(language.DEPENDENCIES_INSTALLED)
    except Exception as e:
        print(e)
        input(language.ERR_ENTER_TO_EXIT)
        return False
    return True
