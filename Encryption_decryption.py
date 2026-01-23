import time
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from aes_engine import *
from hybrid_encryption import *
from digital_signature import *

def encrypt_decrypt_demo(file_data):
    print("\n--------------------CBC Mode Selected--------------------")
    start_time = time.time()
    key = get_random_bytes(16) # AES-128
    encrypted_data, iv = aes_encrypt_cbc(file_data, key)
    end_time = time.time()
    print(f"CBC Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
    start_time = time.time()
    decrypted_data = aes_decrypt_cbc(encrypted_data, iv, key)
    end_time = time.time()
    print(f"CBC Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")

    print("\n--------------------CTR Mode Selected--------------------")
    start_time = time.time()
    key = get_random_bytes(16) 
    encrypted_data, nonce = aes_encrypt_ctr(file_data, key)
    end_time = time.time()
    print(f"CTR Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
    start_time = time.time()
    decrypted_data = aes_decrypt_ctr(encrypted_data, nonce, key)
    end_time = time.time()
    print(f"CTR Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")

    print("\n--------------------CFB Mode Selected--------------------")
    start_time = time.time()
    key = get_random_bytes(16) 
    encrypted_data, iv = aes_encrypt_cfb(file_data, key)
    end_time = time.time()
    print(f"CFB Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
    start_time = time.time()
    decrypted_data = aes_decrypt_cfb(encrypted_data, iv, key)
    end_time = time.time()
    print(f"CFB Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")

    print("\n--------------------OFB Mode Selected--------------------")
    start_time = time.time()
    key = get_random_bytes(16) 
    encrypted_data, iv = aes_encrypt_ofb(file_data, key)
    end_time = time.time()
    print(f"OFB Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
    start_time = time.time()
    decrypted_data = aes_decrypt_ofb(encrypted_data, iv, key)
    end_time = time.time()
    print(f"OFB Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")

    print("\n--------------------GCM Mode Selected--------------------")
    start_time = time.time()
    key = get_random_bytes(16) 
    encrypted_data, nonce, tag = aes_encrypt_gcm(file_data, key)
    end_time = time.time()
    print(f"GCM Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
    start_time = time.time()
    decrypted_data = aes_decrypt_gcm(encrypted_data, nonce, key, tag)
    end_time = time.time()
    print(f"GCM Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")

    print("\n--------------------Hybrid Encryption Selected--------------")
    start_time = time.time()
    rsa_key = RSA.generate(2048)
    private_key = rsa_key.export_key()
    public_key = rsa_key.publickey().export_key()
    encrypted_data = encrypt_content(file_data, public_key)
    end_time = time.time()
    print(f"Hybrid Encryption Time Taken: {end_time - start_time:.4f} seconds")
    start_time = time.time()
    decrypted_data = decrypt_content(encrypted_data, private_key)
    end_time = time.time()
    print(f"Hybrid Decryption Time Taken: {end_time - start_time:.4f} seconds")

    print("\n------------------------------End of Processing for this file -------------------------------")

    return 0