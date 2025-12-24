# Task 2: Robust Hybrid Encryption System
# Implement the full process for content encryption using AES-256-GCM and key wrapping using RSA-OAEP.

# encrypt_content(content_bytes, rsa_public_key): Must generate a random, ephemeral AES key, encrypt the content with AES-GCM, and encrypt the AES key with the public RSA key.
# decrypt_content(encrypted_blob, rsa_private_key): Must reverse the flow, decrypting the AES key first, then decrypting the content and validating the GCM tag.

from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from aes_engine import aes_encrypt_gcm, aes_decrypt_gcm

# Function to encrypt content using AES-256-GCM and wrap the AES key using RSA-OAEP
def encrypt_content(content_bytes, rsa_public_key):
    # Generate random AES key
    aes_key = get_random_bytes(32)

    # Encrypt content using AES-GCM
    encrypted_gcm, nonce_gcm, tag_gcm = aes_encrypt_gcm(content_bytes, aes_key)

    # Encrypt AES key using RSA-OAEP
    rsa_public_key = RSA.import_key(rsa_public_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_public_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    return {
        'encrypted_key' : encrypted_aes_key,
        'nonce' : nonce_gcm,
        'tag' : tag_gcm,
        'ciphertext' : encrypted_gcm
   }
    
# Function to decrypt content using RSA-OAEP and AES-256-GCM
def decrypt_content(encrypted_blob, rsa_private_key):
    encrypted_aes_key = encrypted_blob['encrypted_key']
    nonce_gcm = encrypted_blob['nonce']
    tag_gcm = encrypted_blob['tag']
    ciphertext = encrypted_blob['ciphertext']

    # Decrypt AES key using RSA-OAEP
    rsa_private_key = RSA.import_key(rsa_private_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_private_key)
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)

    # Decrypt content using AES-GCM
    decrypt_content = aes_decrypt_gcm(ciphertext, nonce_gcm, aes_key, tag_gcm)

    return decrypt_content



