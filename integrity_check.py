import hashlib

def calculate_sha256(file_path):
    """
    Calculates the SHA-256 hash of a file.
    :param file_path: Path to the file.
    :return: Hexadecimal SHA-256 hash of the file.
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def verify_file_integrity(original_file, decrypted_file):
    """
    Verifies if the decrypted file matches the original file using SHA-256 hash.
    :param original_file: Path to the original file.
    :param decrypted_file: Path to the decrypted file.
    :return: Boolean indicating whether the files match.
    """
    original_hash = calculate_sha256(original_file)
    decrypted_hash = calculate_sha256(decrypted_file)
    
    return original_hash == decrypted_hash
