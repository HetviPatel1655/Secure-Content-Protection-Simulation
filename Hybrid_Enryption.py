# Task 2: Robust Hybrid Encryption System
# Implement the full process for content encryption using AES-256-GCM and key wrapping using RSA-OAEP.

# encrypt_content(content_bytes, rsa_public_key): Must generate a random, ephemeral AES key, encrypt the content with AES-GCM, and encrypt the AES key with the public RSA key.
# decrypt_content(encrypted_blob, rsa_private_key): Must reverse the flow, decrypting the AES key first, then decrypting the content and validating the GCM tag.

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS7_OAEP
from Crypto.Util.Padding import pad,unpad
from AES_Engine import aes_encrypt_gcm, aes_decrypt_gcm

# Function to encrypt content using AES-256-GCM and wrap the AES key using RSA-OAEP
def encrypt_content(content_bytes, rsa_public_key):
    # Generate random AES key
    aes_key = get_random_bytes(32)

    # Encrypt content using AES-GCM
    cip
    

data = 'This is a test message for Robust Hybrid Encryption System!'.encode()
public_key = RSA.import_key(open('public.pem').read())
private_key = RSA.import_key(open('private.pem').read())

