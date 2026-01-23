from file_utils import FileHandler
from aes_engine import *
import time
    
def decrypt_file_from_chunks(encrypted_container_path, key_size):

    print(f"\n---------- Starting decryption of file of size: {round(len(encrypted_container_path)/(1024*1024), 2)} MB ----------")
    decrypted_chunks = []
    start_time = time.time()

    try:
        encrypted_container_path.sort(key=lambda x: x['index'])
        for chunk_index, row in enumerate(encrypted_container_path):
            key = row['key']
            try:
                decrypted_data = aes_decrypt_ctr(row['ciphertext'], row['nonce'], key)
                decrypted_chunks.append(decrypted_data)
            except Exception as e:
                print(f"Error during decryption of chunk at index {chunk_index}: {e}")
                continue
        decrypted_chunks = b''.join(decrypted_chunks)
        end_time = time.time()
        print(f"\nCTR Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")
        return decrypted_chunks
    except Exception as e:
        raise IOError(f"Error during decryption process: {e}")
    
