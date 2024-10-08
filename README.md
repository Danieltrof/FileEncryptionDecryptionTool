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


