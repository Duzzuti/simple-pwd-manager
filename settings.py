n = 18      # affects time and memory (is used as 2**n)
r = 32      # affects memory and with n also time
p = 1       # affects time
pwdLenBytes = 8    # length of the argument which holds the length of the password section in bytes
saltLenBytes = 16
extension = ".enc"
# has to be in the format "vx.y.z" where x and y are chars (0-255)
# changing the version number will lead to unexpected behavior and could lead to corrupted files
# especially when the goal is to fake an update to be entitled to decrypt some newer version files
version = "v0.1.3"