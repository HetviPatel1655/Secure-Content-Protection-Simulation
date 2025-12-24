import os
from aes_engine import *
from hybrid_encryption import *
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from digital_signature import *

def print_sizes(stage, before=None, after=None):
    print(f"\n[{stage}]")
    if before is not None:
        print("Input size :", before, "bytes")
    if after is not None:
        print("Output size:", after, "bytes")


print("\nAES Encryption/Decryption Demo with Multiple Modes")

print("\nEnter the number of Mode that you want to use for AES Encryption/Decryption:")
print("\n1. CBC Mode\n2. CTR Mode\n3. CFB Mode\n4. OFB Mode\n5. GCM Mode\n6. Hybrid Encryption (RSA + AES)\n")
mode = int(input("Enter your choice (1-6): "))

print("\nEnter the file name that you want to encrypt:")
file_name = input("File name: ")
if not file_name:
    print("No file name provided. Exiting.")
    exit()
elif not os.path.isfile(file_name):
    print("File does not exist. Exiting.")
    exit()
else:
    with open(file_name, 'rb') as f:
        file_data = f.read()
    if not file_data:
        print("File is empty or could not be read. Exiting.")
        exit()  

if (mode == 1):
    print("\nCBC Mode Selected.")
    key = get_random_bytes(16) # AES-128
    encrypted_data, iv = aes_encrypt_cbc(file_data, key)
    decrypted_data = aes_decrypt_cbc(encrypted_data, iv, key)
    print_sizes("CBC Encryption", before=len(file_data), after=len(encrypted_data))
    print_sizes("CBC Decryption", after=len(decrypted_data))
elif (mode) == 2:
    print("\nCTR Mode Selected.")
    key = get_random_bytes(16) 
    encrypted_data, nonce = aes_encrypt_ctr(file_data, key)
    decrypted_data = aes_decrypt_ctr(encrypted_data, nonce, key)
    print_sizes("CTR Encryption", before=len(file_data), after=len(encrypted_data))
    print_sizes("CTR Decryption", after=len(decrypted_data))
elif (mode) == 3:
    print("\nCFB Mode Selected.")
    key = get_random_bytes(16) 
    encrypted_data, iv = aes_encrypt_cfb(file_data, key)
    print_sizes("CFB Encryption", before=len(file_data), after=len(encrypted_data))
    decrypted_data = aes_decrypt_cfb(encrypted_data, iv, key)
    print_sizes("CFB Decryption", after=len(decrypted_data))
elif (mode) == 4:
    print("\nOFB Mode Selected.")
    key = get_random_bytes(16) 
    encrypted_data, iv = aes_encrypt_ofb(file_data, key)
    print_sizes("OFB Encryption", before=len(file_data), after=len(encrypted_data))
    decrypted_data = aes_decrypt_ofb(encrypted_data, iv, key)
    print_sizes("OFB Decryption", after=len(decrypted_data))
elif (mode) == 5:
    print("\nGCM Mode Selected.")
    key = get_random_bytes(16) 
    encrypted_data, nonce, tag = aes_encrypt_gcm(file_data, key)
    print_sizes("GCM Encryption", before=len(file_data), after=len(encrypted_data))
    decrypted_data = aes_decrypt_gcm(encrypted_data, nonce, key, tag)
    print_sizes("GCM Decryption", after=len(decrypted_data))
elif (mode) == 6:
    print("\nHybrid Encryption Selected.")
    rsa_key = RSA.generate(2048)
    private_key = rsa_key.export_key()
    public_key = rsa_key.publickey().export_key()
    encrypted_data = encrypt_content(file_data, public_key)
    print_sizes("Hybrid Encryption", before=len(file_data), after=len(encrypted_data['ciphertext']))
    decrypted_data = decrypt_content(encrypted_data, private_key)
    print_sizes("Hybrid Decryption", after=len(decrypted_data))
else:
    print("\nInvalid choice. Exiting.")
    exit()

if mode != 6:
    with open('encrypted_output.bin', 'wb') as f:
        f.write(encrypted_data)
    with open('decrypted_output.bin', 'wb') as f:
        f.write(decrypted_data)
    print("\nEncryption and Decryption completed. \nCheck 'encrypted_output.bin' and 'decrypted_output.bin'.\n")
else:
    print("\nHybrid encryption and decryption completed. \nCheck 'decrypted_output.bin'.\n")

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
