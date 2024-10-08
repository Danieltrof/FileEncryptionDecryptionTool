# File Encryption and Decryption Tool

## Overview

This project provides a simple command-line tool for encrypting and decrypting files using the **AES (Advanced Encryption Standard)** algorithm in **CBC mode**. Additionally, the tool provides functionality for verifying the integrity of decrypted files by using **SHA-256 hashing**. The tool supports both encryption and decryption using a 256-bit key, ensuring the security and integrity of the files processed.

---

## Features

- **AES Encryption (CBC Mode)**: Encrypt your files using a secure 256-bit AES key.
- **AES Decryption (CBC Mode)**: Decrypt previously encrypted files using the same key.
- **Key Generation**: Automatically generate a 256-bit encryption key if one is not provided.
- **File Integrity Check**: Verify if the decrypted file matches the original using a SHA-256 hash.
- **Modular Design**: The project is structured into separate modules for key generation, encryption/decryption, and file integrity checking.

---

## Requirements

Before running the project, ensure you have the following dependencies installed:

1. **Python 3.x**
2. **PyCryptodome** library for AES encryption.

You can install the required library using pip:
"pip install pycryptodome"

## Module Overview
- **keygen.py:** Responsible for generating a 256-bit AES encryption key.
- **encryption.py:** Handles encryption and decryption of files using AES-CBC
- **integrity_check.py:** Uses SHA-256 to verify file integrity by comparing the original file and the decrypted file
- **main.py:** Primary script to execute the encryption/decryption operations and file integrity checks

## Usage
### Encrypting a file
To encrypt a file, you can run the following command:
python main.py encrypt <file_path>

This will encrypt the specified file. If no encryption key is provided, a new 256-bit key will be generated and displayed in hexadecimal format. Make sure to save this key, as it will be required for decryption :)
E.g:
python main.py encrypt test.txt

Output:
Generated Key (hex): 1f8e1d7fbdc8cbe924e35791a04bf9257294d2a6f5127c3ff45d292d3f7131f5
File encrypted successfully! Encrypted file: test.txt.enc

### Decrypting a file
To decrypt a previously encrypted file, use the following command:
python main.py decrypt <encrypted_file_path> -- key <your_hex_key>
E.g:
python main.py decrypt test.txt.enc --key 1f8e1d7fbdc8cbe924e35791a04bf9257294d2a6f5127c3ff45d292d3f7131f5

#### Notice 
When decrypting a file, the tool checks if the decrypted file matches the original file automatically. It was supposed to only do this when using the --original argument, but I have been too lazy to fix this issue. The error message in terminal will not interfere with the decryption of the file.  
