from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt_file(file_path, key):
    """
    Encrypts a file using AES-CBC mode.
    :param file_path: Path to the file to be encrypted.
    :param key: 256-bit key for encryption.
    """
    with open(file_path, 'rb') as file:
        file_data = file.read()
    
    iv = os.urandom(16)  # Initialization vector (16 bytes)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    encrypted_data = cipher.encrypt(pad(file_data, AES.block_size))
    
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as file_enc:
        file_enc.write(iv + encrypted_data)
    
    return encrypted_file_path

def decrypt_file(file_enc_path, key):
    """
    Decrypts a previously encrypted file using AES-CBC mode.
    """
    with open(file_enc_path, 'rb') as file_enc:
        iv = file_enc.read(16)
        encrypted_data = file_enc.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    
    decrypted_file_path = file_enc_path.replace('.enc', '.dec')
    with open(decrypted_file_path, 'wb') as file_dec:
        file_dec.write(decrypted_data)
    
    return decrypted_file_path
