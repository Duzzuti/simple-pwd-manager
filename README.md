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
5. Run the program using 
    ```bash 
    python main.py
    ``` 
    or double-click on `main.py` if you have associated `.py` files with Python.
6. You can also create a shortcut to `main.py` on your desktop or taskbar for easy access.

## Technical Details
- Files are encrypted using AES-256-CBC in combination with PBKDF2 for key derivation.
- Files are signed using HMAC-SHA256.
- python's `cryptography` library is used for encryption and decryption.
