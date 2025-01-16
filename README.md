# simple-pwd-manager
A simple password manager written in Python.

## Getting Started
0. Make sure you have Python3 installed ([Download Python](https://www.python.org/downloads/))
1. Download the latest release from the [releases page](https://github.com/Duzzuti/simple-pwd-manager/releases/)
2. Extract the downloaded archive.
3. Start the program by running `main.py`
    <br><sub>(1. Note that python must be accessible via `py`,  `python3`, or `python` in your PATH)</sub><br>
    <sub>(2. You can run `.py` files by double clicking or running `python main.py`, `py main.py` or `python3 main.py` in a terminal)</sub><br>
    <sub>(3. Note that dependencies are installed automatically if they are missing)</sub>
4. You can also create a shortcut to `main.py` on your desktop or taskbar for easy access.

## Technical Details
- Files are encrypted using AES-256-CBC in combination with PBKDF2 for key derivation.
- Files are signed using HMAC-SHA256.
- python's `cryptography` library is used for encryption and decryption algorithms.
- iv and salt are generated using `os.urandom()`. <br><sub>(Note that this does not have to be cryptographically secure, it is written to the file in plaintext anyway.)</sub>
- The parameter of the key derivation function can be adjusted and are stored in the `settings.py` file.
- The file stores all information needed for decryption.<br><sub>(This includes the salt, iv, HMAC value, and the parameters for key derivation as well as the version of the software)</sub>
- Random padding is added to the decrypted data to avoid leaking information about the length of the file.
- More detailed information about the file format can be found in the [`encFileFormat.md`](encFileFormat.md) file.
