import argparse
from keygen import generate_key
from encryption import encrypt_file, decrypt_file
from integrity_check import verify_file_integrity

def main():
    parser = argparse.ArgumentParser(description='File Encryption and Decryption Tool')
    
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help='Action to perform: encrypt or decrypt a file')
    parser.add_argument('file', help='Path to the file to encrypt/decrypt')
    parser.add_argument('--key', help='256-bit encryption key in hexadecimal', required=False)
    
    args = parser.parse_args()
    
    if args.action == 'encrypt':
        if args.key:
            key = bytes.fromhex(args.key)
        else:
            key = generate_key()
            print(f'Generated Key (hex): {key.hex()}')
        
        encrypted_file_path = encrypt_file(args.file, key)
        print(f'File encrypted successfully! Encrypted file: {encrypted_file_path}')
    
    elif args.action == 'decrypt':
        if not args.key:
            print("Error: Decryption requires a key.")
            return
        
        key = bytes.fromhex(args.key)
        decrypted_file_path = decrypt_file(args.file, key)
        print(f'File decrypted successfully! Decrypted file: {decrypted_file_path}')
        
        # Verify integrity
        original_file = args.file.replace('.enc', '')  # Assumes original file had same name without .enc
        if verify_file_integrity(original_file, decrypted_file_path):
            print("File integrity check passed. Decrypted file matches the original.")
        else:
            print("File integrity check failed. Decrypted file does not match the original.")
    
if __name__ == '__main__':
    main()
