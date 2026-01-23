from Crypto.Random import get_random_bytes
from aes_engine import *
from hybrid_encryption import *
import os
import time

# # print("\n\nDividing video file into chunks for encryption/decryption...\n")

# # def chunk_size(file_size):
# #     MB = 1024 * 1024
# #     if file_size <= 25 * MB:  # up to 10 MB
# #         return [64 * 1024, 1 * MB]  # 64 KB, 1mb
# #     elif file_size <= 110 * MB:  # up to 100 MB
# #         return 1 * MB, 4 * MB  # 1 MB, 4mb
# #     else :  # rest files
# #         return 4 * MB, 20 * MB  # 4 MB, 20mb

# # Test_files = ["Test Video 10MB.mp4", "Test Video 50MB.mp4", "Test Video 100MB.mp4",
# #               "Test Video 500MB.mp4", "Test Video 800MB.mp4", "Test Video 1GB.mp4"]

# # MODES = ['CBC', 'CTR', 'CFB', 'OFB', 'GCM', 'Hybrid']

# for file_path in Test_files:
#     print("\n" + "="*100)
#     file_size = os.path.getsize(file_path)
#     print("\nFile size(in mb):", file_size/(1024*1024))
#     print(f"\nProcessing file of size: {file_size/(1024 * 1024)} MB in chunks")

#     with open(file_path, 'rb') as f:
#         file_data = f.read()

#     chunk_size_1,chunk_size_2 = chunk_size(file_size)
#     print(f"Using chunk size: {chunk_size_1/(1024*1024)} MB and {chunk_size_2/(1024*1024)} MB for processing.")
#     # Further implementation needed to process file_data in chunks
#     print(f"\n--------------------CTR Mode Selected--------------------")
#     start_time = time.time()
#     encrypted_storage = []
    
#     for i in range(0,2):
#         current_chunk_size = chunk_size_1 if i==0 else chunk_size_2
#         print(f"\nProcessing with chunk size: {current_chunk_size/(1024*1024)} MB")
#         for i in range(0, len(file_data), current_chunk_size):
#             chunk = file_data[i:i+current_chunk_size]
#             key = get_random_bytes(16)  # New key for each chunk
#             encrypted_data, nonce = aes_encrypt_ctr(chunk, key)
#             row = {
#                 'index': i,
#                 'key': key, 
#                 'nonce': nonce, 
#                 'ciphertext': encrypted_data
#             }
#             encrypted_storage.append(row)

#         end_time = time.time()
#         print(f"CTR Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")

#     #store the encrypted data along with keys and nonces for decryption later in sample file that will be the input to the decryption.py file 

    
def encrypt_file_in_chunks(input_bytes, chunk_size, key_size):
    if not input_bytes:
        raise ValueError("Input file bytes cannot be empty.")

    encrypted_storage = []
    input_size = len(input_bytes)

    print(f"\n---------- Starting encryption of file of size: {round(input_size/(1024*1024), 2)} MB ----------")
    start_time = time.time()
    
    try:
        chunk_index = 0
        # print(f"Processing with chunk size: {chunk_size/(1024*1024)} MB")
        for i in range(0, len(input_bytes), chunk_size):
            chunk = input_bytes[i:i+chunk_size]
            key = get_random_bytes(key_size // 8)  # New key for each chunk
            encrypted_data, nonce = aes_encrypt_ctr(chunk, key)
            row = {
                'index': i,
                'key': key, 
                'nonce': nonce, 
                'ciphertext': encrypted_data
            }
            encrypted_storage.append(row)
            chunk_index += 1
        
        end_time = time.time()
        print(f"\nCTR Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
        return encrypted_storage
    
    except Exception as e:
        raise RuntimeError(f"An error occurred during encryption: {e}")
    
