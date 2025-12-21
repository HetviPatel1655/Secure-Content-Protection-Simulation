from AES_Engine import *

from Crypto.Random import get_random_bytes

print("\nAES Encryption/Decryption Example : ")
key = get_random_bytes(16) # AES-128
data = 'This is a test message for AES encryption!'.encode()
print("\nOriginal Data:", data)

# CBC Mode
encrypted_cbc, encrypted_cbc_iv = aes_encrypt_cbc(data, key)
print("\nCBC Encrypted:", encrypted_cbc)
decrypted_cbc = aes_decrypt_cbc(encrypted_cbc, encrypted_cbc_iv, key)
print("CBC Decrypted:", decrypted_cbc)

# CTR Mode
encrypted_ctr, nonce_ctr = aes_encrypt_ctr(data, key)
print("\nCTR Encrypted:", encrypted_ctr)
decrypted_ctr = aes_decrypt_ctr(encrypted_ctr, nonce_ctr, key)
print("CTR Decrypted:", decrypted_ctr)

#CFB Mode
encrypted_cfb, encrypted_cfb_iv = aes_encrypt_cfb(data, key)
print("\nCFB Encrypted: ", encrypted_cfb)
decrypted_cfb = aes_decrypt_cfb(encrypted_cfb, encrypted_cfb_iv, key)
print("CFB Decrypted:", decrypted_cfb) 

#OFB Mode
encrypted_ofb, encrypted_ofb_iv = aes_encrypt_ofb(data, key)
print("\nOFB Encrypted: ",encrypted_ofb)
decrypted_ofb = aes_decrypt_ofb(encrypted_ofb, encrypted_ofb_iv, key)
print("OFB Decrypted:",decrypted_ofb)

#GCM Mode
encrypted_gcm, nonce_gcm, tag = aes_encrypt_gcm(data, key)
print("\nGCM Encrypted: ", encrypted_gcm)
decrypted_gcm = aes_decrypt_gcm(encrypted_gcm, nonce_gcm, key, tag)
print("GCM Decrypted:", decrypted_gcm)