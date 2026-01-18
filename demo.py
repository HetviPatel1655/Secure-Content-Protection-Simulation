import os
from aes_engine import *
from hybrid_encryption import *
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from digital_signature import *
import time
from Encryption_decryption import encrypt_decrypt_demo 

# def print_sizes(stage, before=None, after=None):
#     print(f"\n[{stage}]")
#     if before is not None:
#         print("Input size :", before, "bytes")
#     if after is not None:
#         print("Output size:", after, "bytes")

print("\nAES Encryption/Decryption Demo with Multiple Modes")

Test_files = ["Test Video 10MB.mp4", "Test Video 25MB.mp4", "Test Video 50MB.mp4",
              "Test Video 100MB.mp4", "Test Video 500MB.mp4", "Test Video 800MB.mp4",
              "Test Video 1GB.mp4"]

# Change index to test different sizes
# for file_path in Test_files:
#     print("\n" + "="*100)
#     file_size = os.path.getsize(file_path)
#     print("\nFile size(in mb):", file_size/(1024*1024))
#     print(f"\nProcessing file of size: {file_size} bytes")

#     with open(file_path, 'rb') as f:
#         file_data = f.read()

#     encrypt_decrypt_demo(file_data)

# Processing the video file as a whole for encryption/decryption

# print("\n--------------------CBC Mode Selected--------------------")
# start_time = time.time()
# key = get_random_bytes(16) # AES-128
# encrypted_data, iv = aes_encrypt_cbc(file_data, key)
# end_time = time.time()
# print(f"CBC Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
# start_time = time.time()
# decrypted_data = aes_decrypt_cbc(encrypted_data, iv, key)
# end_time = time.time()
# print(f"CBC Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")

# print("\n--------------------CTR Mode Selected--------------------")
# start_time = time.time()
# key = get_random_bytes(16) 
# encrypted_data, nonce = aes_encrypt_ctr(file_data, key)
# end_time = time.time()
# print(f"CTR Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
# start_time = time.time()
# decrypted_data = aes_decrypt_ctr(encrypted_data, nonce, key)
# end_time = time.time()
# print(f"CTR Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")

# print("\n--------------------CFB Mode Selected--------------------")
# start_time = time.time()
# key = get_random_bytes(16) 
# encrypted_data, iv = aes_encrypt_cfb(file_data, key)
# end_time = time.time()
# print(f"CFB Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
# start_time = time.time()
# decrypted_data = aes_decrypt_cfb(encrypted_data, iv, key)
# end_time = time.time()
# print(f"CFB Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")

# print("\n--------------------OFB Mode Selected--------------------")
# start_time = time.time()
# key = get_random_bytes(16) 
# encrypted_data, iv = aes_encrypt_ofb(file_data, key)
# end_time = time.time()
# print(f"OFB Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
# start_time = time.time()
# decrypted_data = aes_decrypt_ofb(encrypted_data, iv, key)
# end_time = time.time()
# print(f"OFB Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")

# print("\n--------------------GCM Mode Selected--------------------")
# start_time = time.time()
# key = get_random_bytes(16) 
# encrypted_data, nonce, tag = aes_encrypt_gcm(file_data, key)
# end_time = time.time()
# print(f"GCM Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
# start_time = time.time()
# decrypted_data = aes_decrypt_gcm(encrypted_data, nonce, key, tag)
# end_time = time.time()
# print(f"GCM Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")

# print("\n--------------------Hybrid Encryption Selected--------------")
# start_time = time.time()
# rsa_key = RSA.generate(2048)
# private_key = rsa_key.export_key()
# public_key = rsa_key.publickey().export_key()
# encrypted_data = encrypt_content(file_data, public_key)
# end_time = time.time()
# print(f"Hybrid Encryption Time Taken: {end_time - start_time:.4f} seconds")
# start_time = time.time()
# decrypted_data = decrypt_content(encrypted_data, private_key)
# end_time = time.time()
# print(f"Hybrid Decryption Time Taken: {end_time - start_time:.4f} seconds")

# print("\n------------------------------End of Processing for this file -------------------------------")

# Dividing video files into chunks for encryption/decryption
# take a file , divide in chunks, take first chunk apply aes mode 1 get the encryptred text and key/iv/nonce take the encrypted text and key separated by delimeter and proceed to next chunk calculate time for whole file for each mode. 

# Load test files into memory

print("\n\nDividing video file into chunks for encryption/decryption...\n")

def chunk_size(file_size):
    MB = 1024 * 1024
    if file_size <= 25 * MB:  # up to 10 MB
        return [64 * 1024, 1 * MB]  # 64 KB, 1mb
    elif file_size <= 110 * MB:  # up to 100 MB
        return 1 * MB, 4 * MB  # 1 MB, 4mb
    else :  # rest files
        return 4 * MB, 20 * MB  # 4 MB, 20mb
    
# Test chunk sizes 64 kb, 1mb, 16mb, 64mb
# chunk_64kb = 64 * 1024  # 64 KB
# chunk_1mb = 1 * 1024 * 1024  # 1 MB
# chunk_4mb = 4 * 1024 * 1024  # 4 MB
# chunk_20mb = 20 * 1024 * 1024  # 20 MB

Test_files = ["Test Video 10MB.mp4", "Test Video 50MB.mp4", "Test Video 100MB.mp4",
              "Test Video 500MB.mp4", "Test Video 800MB.mp4", "Test Video 1GB.mp4"]

MODES = ['CBC', 'CTR', 'CFB', 'OFB', 'GCM', 'Hybrid']

for file_path in Test_files:
    print("\n" + "="*100)
    file_size = os.path.getsize(file_path)
    print("\nFile size(in mb):", file_size/(1024*1024))
    print(f"\nProcessing file of size: {file_size/(1024 * 1024)} MB in chunks")

    with open(file_path, 'rb') as f:
        file_data = f.read()

    chunk_size_1,chunk_size_2 = chunk_size(file_size)
    print(f"Using chunk size: {chunk_size_1/(1024*1024)} MB and {chunk_size_2/(1024*1024)} MB for processing.")
    # Further implementation needed to process file_data in chunks
    for mode in MODES:
        print(f"\n--------------------{mode} Mode Selected--------------------")
        start_time = time.time()
        key = get_random_bytes(16)  # AES-128

        encrypted_storage = []
        
        for i in range(0,2):
            current_chunk_size = chunk_size_1 if i==0 else chunk_size_2
            print(f"\nProcessing with chunk size: {current_chunk_size/(1024*1024)} MB")
            for i in range(0, len(file_data), current_chunk_size):
                chunk = file_data[i:i+current_chunk_size]
                #print(f"chunk number: {i//current_chunk_size + 1}")
                key = get_random_bytes(16)  # New key for each chunk
                if mode == 'CBC':
                    encrypted_data, iv = aes_encrypt_cbc(chunk, key)
                    row = {'index': i, 'mode': mode, 'key': key, 'iv': iv, 'ciphertext': encrypted_data}
                    #decrypted_data = aes_decrypt_cbc(encrypted_data, iv, key)
                elif mode == 'CTR':
                    encrypted_data, nonce = aes_encrypt_ctr(chunk, key)
                    row = {'index': i, 'mode': mode, 'key': key, 'nonce': nonce, 'ciphertext': encrypted_data}
                    #decrypted_data = aes_decrypt_ctr(encrypted_data, nonce, key)
                elif mode == 'CFB':
                    encrypted_data, iv = aes_encrypt_cfb(chunk, key)
                    row = {'index': i, 'mode': mode, 'key': key, 'iv': iv, 'ciphertext': encrypted_data}
                    #decrypted_data = aes_decrypt_cfb(encrypted_data, iv, key)
                elif mode == 'OFB':
                    encrypted_data, iv = aes_encrypt_ofb(chunk, key)
                    row = {'index': i, 'mode': mode, 'key': key, 'iv': iv, 'ciphertext': encrypted_data}
                    #decrypted_data = aes_decrypt_ofb(encrypted_data, iv, key)
                elif mode == 'GCM':
                    encrypted_data, nonce, tag = aes_encrypt_gcm(chunk, key)
                    row = {'index': i, 'mode': mode, 'key': key, 'nonce': nonce, 'tag': tag, 'ciphertext': encrypted_data}
                    #decrypted_data = aes_decrypt_gcm(encrypted_data, nonce, key, tag)
                elif mode == 'Hybrid':
                    rsa_key = RSA.generate(2048)
                    private_key = rsa_key.export_key()
                    public_key = rsa_key.publickey().export_key()
                    encrypted_data = encrypt_content(chunk, public_key)
                    row = {'index': i, 'mode': mode, 'ciphertext': encrypted_data, 'key': private_key}
                    #decrypted_data = decrypt_content(encrypted_data, private_key)
                
                encrypted_storage.append(row)
            #print("\nEncrypted storage sample (first 2 chunks):", encrypted_storage[:2])

            end_time = time.time()
            print(f"{mode} Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")

            # Decryption process
            start_time = time.time()
            for row in encrypted_storage:
                chunk = file_data[row['index']:row['index']+chunk_size_1]
                key = row['key']
                if mode == 'CBC':
                    decrypted_data = aes_decrypt_cbc(row['ciphertext'], row['iv'], key)
                elif mode == 'CTR':
                    decrypted_data = aes_decrypt_ctr(row['ciphertext'], row['nonce'], key)
                elif mode == 'CFB':
                    decrypted_data = aes_decrypt_cfb(row['ciphertext'], row['iv'], key)
                elif mode == 'OFB':
                    decrypted_data = aes_decrypt_ofb(row['ciphertext'], row['iv'], key)
                elif mode == 'GCM':
                    decrypted_data = aes_decrypt_gcm(row['ciphertext'], row['nonce'], key, row['tag'])
                elif mode == 'Hybrid':
                    decrypted_data = decrypt_content(row['ciphertext'], row['key'])
            end_time = time.time()
            print(f"{mode} Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")
    print("\n------------------------------End of Processing for this file -------------------------------")

        