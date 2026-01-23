import os
import encryption
import decryption
from file_utils import FileHandler

# CONFIGURATIONS
TEST_FILES = ["Test Video 10MB.mp4", "Test Video 50MB.mp4", "Test Video 100MB.mp4",
             "Test Video 500MB.mp4", "Test Video 800MB.mp4", "Test Video 1GB.mp4"]
CONTAINER_FILE = "encrypted_data_container.dat"
CHUNK_SIZES = {
    'small': [1 * 1024 * 1024],     # 1 MB
    'medium': [4 * 1024 * 1024],    # 4 MB
    'large': [20 * 1024 * 1024]     # 20 MB
}

def determine_chunk_size(file_size):
    MB = 1024 * 1024
    if file_size <= 25 * MB:
        return CHUNK_SIZES['small']
    elif file_size <= 110 * MB:
        return CHUNK_SIZES['medium']
    else:
        return CHUNK_SIZES['large']
    
def run_pipeline():
    #step 0: ask for key size
    key_size = int(input("\nEnter key size in bits (128, 192, 256): "))
        
    for file_path in TEST_FILES:
        #step 1: Input handling
        # print("\nLoading file:", file_path)
        try:
            raw_bytes = FileHandler.read_file_to_bytes(file_path)
            print(f"\nFile {file_path} loaded successfully, size: {round(len(raw_bytes)/(1024*1024), 2)} MB")
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return
        
        #step 2: Encryption
        file_size = len(raw_bytes)
        chunk_size = determine_chunk_size(file_size)
        print(f"chunk size: {chunk_size[0]/(1024*1024)} MB")
        try:
            encrypted_container = encryption.encrypt_file_in_chunks(raw_bytes, chunk_size[0], key_size)
            # print(f"Encryption completed for file: {file_path}")

            FileHandler.save_encrypted_container(CONTAINER_FILE, encrypted_container)
            del raw_bytes  # Free memory
            del encrypted_container  # Free memory

        except Exception as e:
            print(f"Error during encryption of file {file_path}: {e}")
            return
        
        #step 3: Decryption
        try:
            loaded_container = FileHandler.load_encrypted_container(CONTAINER_FILE)
            # print(f"Loaded encrypted container from {CONTAINER_FILE}")

            decrypted_bytes = decryption.decrypt_file_from_chunks(loaded_container, key_size)
            # print(f"Decryption completed for file: {file_path}")

            # Optionally, write decrypted bytes to a file for verification
            output_file_path = f"decrypted_{os.path.basename(file_path)}"
            FileHandler.write_bytes_to_file(output_file_path, decrypted_bytes)
            print(f"Decrypted file written to: {output_file_path}")

            del loaded_container  # Free memory
            del decrypted_bytes  # Free memory

        except Exception as e:
            print(f"Error during decryption of file {file_path}: {e}")
            return
        print(f"\nPipeline completed for file: {file_path}\n")
        print("="*100)

if __name__ == "__main__":
    run_pipeline()