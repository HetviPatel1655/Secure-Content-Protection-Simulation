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
    return ciphertext, iv  # Prepend IV for use in decryption

# CBC MODE DECRYPTION
def aes_decrypt_cbc(ciphertext, iv, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# CTR MODE ENCRYPTION   
def aes_encrypt_ctr(plaintext, key):
    # 64-bit counter with 64-bit nonce prefix (recommended pattern)
    nonce = get_random_bytes(8)
    ctr = Counter.new(64, prefix=nonce)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext, nonce

# CTR MODE DECRYPTION
def aes_decrypt_ctr(ciphertext, nonce, key):
    ctr = Counter.new(64, prefix=nonce)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

#CFB ENCRYPTION
def aes_encrypt_cfb(plaintext, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key,AES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext, iv

#CFB DECRYPTION
def aes_decrypt_cfb(ciphertext, iv, key):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

#OFB ENCRYPTION
def aes_encrypt_ofb(plaintext, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key,AES.MODE_OFB, iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext, iv

#OFB DECRYPTION
def aes_decrypt_ofb(ciphertext, iv, key):
    cipher = AES.new(key, AES.MODE_OFB, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

#GCM ENCRYPTION
def aes_encrypt_gcm(plaintext, key):
    nonce = get_random_bytes(12)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ciphertext, tag = cipher.encrypt(plaintext), cipher.digest()
    return ciphertext, nonce, tag

#GCM DECRYPTION
def aes_decrypt_gcm(ciphertext, nonce, key, tag):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext