import os
from aes_engine import *
from hybrid_encryption import *
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from digital_signature import *
import time

def print_sizes(stage, before=None, after=None):
    print(f"\n[{stage}]")
    if before is not None:
        print("Input size :", before, "bytes")
    if after is not None:
        print("Output size:", after, "bytes")


print("\nAES Encryption/Decryption Demo with Multiple Modes")

# print("\nEnter the number of Mode that you want to use for AES Encryption/Decryption:")
# print("\n1. CBC Mode\n2. CTR Mode\n3. CFB Mode\n4. OFB Mode\n5. GCM Mode\n6. Hybrid Encryption (RSA + AES)\n")
# mode = int(input("Enter your choice (1-6): "))

# print("\nEnter the file name that you want to encrypt:")
# file_name = input("File name: ")
# if not file_name:
#     print("No file name provided. Exiting.")
#     exit()
# elif not os.path.isfile(file_name):
#     print("File does not exist. Exiting.")
#     exit()
# else:
#     with open(file_name, 'rb') as f:
#         file_data = f.read()
#     if not file_data:
#         print("File is empty or could not be read. Exiting.")
#         exit() 

with open('Test Video 10MB.mp4', 'rb') as f:
    file_data_10mb = f.read()     

with open('Test Video 25MB.mp4', 'rb') as f:
    file_data_25mb = f.read()

with open('Test Video 50MB.mp4', 'rb') as f:
    file_data_50mb = f.read()

with open('Test Video 100MB.mp4', 'rb') as f:
    file_data_100mb = f.read()

with open('Test Video 200MB.mp4', 'rb') as f:
    file_data_200mb = f.read()

with open('Test Video 434MB.mp4', 'rb') as f:
    file_data_434mb = f.read()

with open('Test Video 1664MB.mp4', 'rb') as f:
    file_data_1664mb = f.read()

# file_data = [file_data_10mb, file_data_50mb, file_data_434mb]

 # Change index to test different sizes
for file_data in [file_data_10mb, file_data_25mb, file_data_50mb, file_data_100mb, file_data_200mb, file_data_434mb, file_data_1664mb]:
    print("\n" + "="*100)
    print("\nFile size(in mb):", len(file_data)/(1024*1024))
    print(f"\nProcessing file of size: {len(file_data)} bytes")

# if (mode == 1):
    print("\n--------------------CBC Mode Selected--------------------")
    start_time = time.time()
    key = get_random_bytes(16) # AES-128
    encrypted_data, iv = aes_encrypt_cbc(file_data, key)
    end_time = time.time()
    print(f"CBC Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
    # print_sizes("CBC Encryption", before=len(file_data), after=len(encrypted_data))
    start_time = time.time()
    decrypted_data = aes_decrypt_cbc(encrypted_data, iv, key)
    end_time = time.time()
    print(f"CBC Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")
    # print_sizes("CBC Decryption", after=len(decrypted_data))
#elif (mode) == 2:
    print("\n--------------------CTR Mode Selected--------------------")
    start_time = time.time()
    key = get_random_bytes(16) 
    encrypted_data, nonce = aes_encrypt_ctr(file_data, key)
    end_time = time.time()
    print(f"CTR Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
    # print_sizes("CTR Encryption", before=len(file_data), after=len(encrypted_data))
    start_time = time.time()
    decrypted_data = aes_decrypt_ctr(encrypted_data, nonce, key)
    end_time = time.time()
    print(f"CTR Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")
    # print_sizes("CTR Decryption", after=len(decrypted_data))
#elif (mode) == 3:
    print("\n--------------------CFB Mode Selected--------------------")
    start_time = time.time()
    key = get_random_bytes(16) 
    encrypted_data, iv = aes_encrypt_cfb(file_data, key)
    end_time = time.time()
    print(f"CFB Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
    # print_sizes("CFB Encryption", before=len(file_data), after=len(encrypted_data))
    start_time = time.time()
    decrypted_data = aes_decrypt_cfb(encrypted_data, iv, key)
    end_time = time.time()
    print(f"CFB Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")
    # print_sizes("CFB Decryption", after=len(decrypted_data))
#elif (mode) == 4:
    print("\n--------------------OFB Mode Selected--------------------")
    start_time = time.time()
    key = get_random_bytes(16) 
    encrypted_data, iv = aes_encrypt_ofb(file_data, key)
    end_time = time.time()
    print(f"OFB Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
    # print_sizes("OFB Encryption", before=len(file_data), after=len(encrypted_data))
    start_time = time.time()
    decrypted_data = aes_decrypt_ofb(encrypted_data, iv, key)
    end_time = time.time()
    print(f"OFB Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")
    # print_sizes("OFB Decryption", after=len(decrypted_data))
#elif (mode) == 5:
    print("\n--------------------GCM Mode Selected--------------------")
    start_time = time.time()
    key = get_random_bytes(16) 
    encrypted_data, nonce, tag = aes_encrypt_gcm(file_data, key)
    end_time = time.time()
    print(f"GCM Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
    # print_sizes("GCM Encryption", before=len(file_data), after=len(encrypted_data))
    start_time = time.time()
    decrypted_data = aes_decrypt_gcm(encrypted_data, nonce, key, tag)
    end_time = time.time()
    print(f"GCM Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")
    # print_sizes("GCM Decryption", after=len(decrypted_data))
#elif (mode) == 6:
    print("\n--------------------Hybrid Encryption Selected--------------")
    start_time = time.time()
    rsa_key = RSA.generate(2048)
    private_key = rsa_key.export_key()
    public_key = rsa_key.publickey().export_key()
    encrypted_data = encrypt_content(file_data, public_key)
    end_time = time.time()
    print(f"Hybrid Encryption Time Taken: {end_time - start_time:.4f} seconds")
    # print_sizes("Hybrid Encryption", before=len(file_data), after=len(encrypted_data['ciphertext']))
    start_time = time.time()
    decrypted_data = decrypt_content(encrypted_data, private_key)
    end_time = time.time()
    print(f"Hybrid Decryption Time Taken: {end_time - start_time:.4f} seconds")

    print("\n------------------------------End of Processing for this file -------------------------------")

    # print_sizes("Hybrid Decryption", after=len(decrypted_data))
# else:
#     print("\nInvalid choice. Exiting.")
#     exit()

# if mode != 6:
#     with open('encrypted_output.bin', 'wb') as f:
#         f.write(encrypted_data)
#     with open('decrypted_output.bin', 'wb') as f:
#         f.write(decrypted_data)
#     print("\nEncryption and Decryption completed. \nCheck 'encrypted_output.bin' and 'decrypted_output.bin'.\n")
# else:
#     print("\nHybrid encryption and decryption completed. \nCheck 'decrypted_output.bin'.\n")

# Demonstration of Digital Signature and Verification
# Separate RSA keys used for encryption and signing (recommended practice)

print("\nDigital Signature and Verification Demo\n")
rsa_key = RSA.generate(2048)
private_key = rsa_key.export_key()
public_key = rsa_key.publickey().export_key()

# Sign the data
signature = sign_data(file_data, private_key)
print("Signature generated.")

# Verify the signature (should be valid)
is_valid = verify_signature(file_data, signature, public_key)
print(f"Signature valid: {is_valid}")

# Tamper with the data
tampered_data = file_data[:-1] + bytes([file_data[-1] ^ 0x01])

# Verify the signature with tampered data (should be invalid)
is_valid_tampered = verify_signature(tampered_data, signature, public_key)
print(f"Signature valid after tampering with data: {is_valid_tampered}")

# Tamper with the signature
tampered_signature = signature[:-1] + bytes([signature[-1] ^ 0x01])  # Flip last bit

# Verify the tampered signature (should be invalid)
is_valid_tampered_sig = verify_signature(file_data, tampered_signature, public_key)
print(f"Signature valid after tampering with signature: {is_valid_tampered_sig}")
