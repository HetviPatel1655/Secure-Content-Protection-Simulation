# Task 1: Comprehensive AES Implementation
# Implement functions to encrypt and decrypt a data sample across all five required modes: CBC, CTR, GCM, CFB, and OFB.
# Requirements: Functions must correctly handle unique requirements for each mode, including IV generation, padding (if applicable), and authentication tag (GCM only).

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter

# CBC MODE ENCRYPTION
def aes_encrypt_cbc(plaintext, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext,AES.block_size))
    return iv , ciphertext  # Prepend IV for use in decryption

# CBC MODE DECRYPTION
def aes_decrypt_cbc(iv, ciphertext, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# CTR MODE ENCRYPTION   
def aes_encrypt_ctr(plaintext, key):
    nonce = get_random_bytes(8)
    ctr = Counter.new(64, prefix=nonce)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    ciphertext = cipher.encrypt(plaintext)
    return nonce, ciphertext

# CTR MODE DECRYPTION
def aes_decrypt_ctr(nonce, ciphertext, key):
    ctr = Counter.new(64, prefix=nonce)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

#CFB ENCRYPTION
def aes_encrypt_cfb(plaintext, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key,AES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(plaintext)
    return iv, ciphertext

#CFB DECRYPTION
def aes_decrypt_cfb(iv, ciphertext, key):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

#OFB ENCRYPTION
def aes_encrypt_ofb(plaintext, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key,AES.MODE_OFB, iv)
    ciphertext = cipher.encrypt(plaintext)
    return iv, ciphertext

#OFB DECRYPTION
def aes_decrypt_ofb(iv, ciphertext, key):
    cipher = AES.new(key, AES.MODE_OFB, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

