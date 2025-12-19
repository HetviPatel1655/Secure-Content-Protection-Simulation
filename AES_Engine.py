# Task 1: Comprehensive AES Implementation
# Implement functions to encrypt and decrypt a data sample across all five required modes: CBC, CTR, GCM, CFB, and OFB.
# Requirements: Functions must correctly handle unique requirements for each mode, including IV generation, padding (if applicable), and authentication tag (GCM only).

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter

def aes_encrypt_cbc(plaintext, key):
    print("Encrypting in CBC mode")
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext,AES.block_size))
    return iv + ciphertext  # Prepend IV for use in decryption

def aes_decrypt_cbc(ciphertext, key):
    print("Decrypting in CBC mode")
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
    return plaintext


print("AES Encryption/Decryption Example : ")
key = get_random_bytes(16) # AES-128
data = b'This is a test message for AES encryption!'
print("Original Data:", data)

# CBC Mode
encrypted_cbc = aes_encrypt_cbc(data, key)
print("CBC Encrypted:", encrypted_cbc)
decrypted_cbc = aes_decrypt_cbc(encrypted_cbc, key)
print("CBC Decrypted:", decrypted_cbc)

