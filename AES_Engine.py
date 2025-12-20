# Task 1: Comprehensive AES Implementation
# Implement functions to encrypt and decrypt a data sample across all five required modes: CBC, CTR, GCM, CFB, and OFB.
# Requirements: Functions must correctly handle unique requirements for each mode, including IV generation, padding (if applicable), and authentication tag (GCM only).

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter

# CBC MODE ENCRYPTION
def aes_encrypt_cbc(plaintext, key):
    print("Encrypting in CBC mode")
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext,AES.block_size))
    return iv , ciphertext  # Prepend IV for use in decryption

# CBC MODE DECRYPTION
def aes_decrypt_cbc(iv, ciphertext, key):
    print("Decrypting in CBC mode")
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# CTR MODE ENCRYPTION   
def aes_encrypt_ctr(plaintext, key):
    print("Encrypting in CTR mode")
    nonce = get_random_bytes(8)
    ctr = Counter.new(64, prefix=nonce)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext,nonce

# CTR MODE DECRYPTION
def aes_decrypt_ctr(nonce, ciphertext, key):
    print("Decrypting in CTR mode")
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


print("AES Encryption/Decryption Example : ")
key = get_random_bytes(16) # AES-128
data = b'This is a test message for AES encryption!'
print("Original Data:", data)

# CBC Mode
encrypted_cbc_iv, encrypted_cbc = aes_encrypt_cbc(data, key)
print("CBC Encrypted:", encrypted_cbc)
decrypted_cbc = aes_decrypt_cbc(encrypted_cbc_iv , encrypted_cbc, key)
print("CBC Decrypted:", decrypted_cbc)

# CTR Mode
encrypted_ctr, nonce = aes_encrypt_ctr(data, key)
print("CTR Encrypted:", encrypted_ctr)
decrypted_ctr = aes_decrypt_ctr(nonce, encrypted_ctr, key)
print("CTR Decrypted:", decrypted_ctr)

#CFB Mode
encrypted_cfb_iv, encrypted_cfb = aes_encrypt_cfb(data, key)
print("CFB Encrypted: ", encrypted_cfb)
decrypted_cfb = aes_decrypt_cfb(encrypted_cfb_iv, encrypted_cfb, key)
print("CFB Decrypted:", decrypted_cfb) 