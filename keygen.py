from Crypto.Random import get_random_bytes

def generate_key():
    """ 
    Genererer en 256-bit key for AES encryption
    """
    return get_random_bytes(32) 

