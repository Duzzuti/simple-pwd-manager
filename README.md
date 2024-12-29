# simple-pwd-manager
A simple password manager written in Python.

## Getting Started
0. Make sure you have Python3 installed ([Download Python](https://www.python.org/downloads/))
1. Download the latest release from the [releases page](https://github.com/Duzzuti/simple-pwd-manager/releases/)
2. Extract the downloaded archive.
3. Open a terminal in the extracted folder.
4. Install the required dependencies using <br>

    ```bash 
    pip install -r requirements.txt
    ```
    or 
    ```bash
    python -m pip install -r requirements.txt
    ```
    <sub>(If this does not work try `python3` or `py` instead of `python`)</sub>
5. Run the program using 
    ```bash 
    python main.py
    ```
    or double-click on `main.py` if you have associated `.py` files with Python.
6. You can also create a shortcut to `main.py` on your desktop or taskbar for easy access.

## Technical Details
- Files are encrypted using AES-256-CBC in combination with PBKDF2 for key derivation.
- Files are signed using HMAC-SHA256.
- python's `cryptography` library is used for encryption and decryption algorithms.
- iv and salt are generated using `os.urandom()`. <br><sub>(Note that this does not have to be cryptographically secure, it is written to the file in plaintext anyway.)</sub>
- The parameter of the key derivation function can be adjusted and are stored in the `settings.py` file.
- The file stores all information needed for decryption.<br><sub>(This includes the salt, iv, HMAC value, and the parameters for key derivation as well as the version of the software)</sub>
- Random padding is added to the decrypted data to avoid leaking information about the length of the file.
- More detailed information about the file format can be found in the [`encFileFormat.md`](encFileFormat.md) file.