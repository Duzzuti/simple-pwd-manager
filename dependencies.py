import os

def installDependencies():
    try:
        pythonNames = ["py", "python", "python3"]
        for name in pythonNames:
            # download new dependencies
            if os.system(name + " -m pip install -r requirements.txt") == 0:
                break
        else:
            print("Could not install the required packages, because no python installation found.\nPlease make sure python is accessible with 'py', 'python' or 'python3' or install the dependencies manually with \n'python -m pip install -r requirements.txt'")
            input("Press enter to exit...")
            return False
        print("Dependencies installed. You can now run the program.")
    except Exception as e:
        print(e)
        input("An error occurred. Press enter to exit...")
        return False
    return True
