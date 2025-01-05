import languages

language = languages.loadLanguage()

n = 18      # affects time and memory (is used as 2**n)
r = 32      # affects memory and with n also time
p = 1       # affects time
pwdLenBytes = 8    # length of the argument which holds the length of the password section in bytes
saltLenBytes = 16
extension = ".enc"
# has to be in the format "vx.y.z" where x and y are chars (0-255)
# changing the version number will lead to unexpected behavior and could lead to corrupted files
# especially when the goal is to fake an update to be entitled to decrypt some newer version files
version = "v0.1.5"

def isFileCompatible(majorVersion, minorVersion) -> bool:
    majorVersion = int(majorVersion)
    minorVersion = int(minorVersion)
    programMajor = int(version[1:].split(".")[0])
    programMinor = int(version.split(".")[1])
    if majorVersion > programMajor:
        return False
    if majorVersion == programMajor and minorVersion > programMinor:
        return False
    return True

def isVersionNewer(newVersion : str) -> bool:
    newVersionMajor = int(newVersion[1:].split(".")[0])
    programMajor = int(version[1:].split(".")[0])
    if newVersionMajor > programMajor:
        return True
    elif newVersionMajor == programMajor:
        newVersionMinor = int(newVersion.split(".")[1])
        programMinor = int(version.split(".")[1])
        if newVersionMinor > programMinor:
            return True
        elif newVersionMinor == programMinor:
            if len(newVersion.split(".")) == 3:  
                newVersionPatch = int(newVersion.split(".")[2])
            else:
                newVersionPatch = 0
            if len(version.split(".")) == 3:
                programPatch = int(version.split(".")[2])
            else:
                programPatch = 0
            return newVersionPatch > programPatch
    return False