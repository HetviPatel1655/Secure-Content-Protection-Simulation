import os
import pickle

class FileHandler:
    @staticmethod
    def read_file_to_bytes(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        try:
            with open(file_path, 'rb') as file:
                return file.read()
        except MemoryError:
            raise MemoryError(f"File {file_path} is too large to fit into memory.")
        except IOError as e:
            raise IOError(f"An error occurred while reading the file {file_path}: {e}")
                  
    @staticmethod
    def write_bytes_to_file(file_path, data):
        try:
            with open(file_path, 'wb') as file:
                file.write(data)
        except IOError as e:
            raise IOError(f"An error occurred while writing to the file {file_path}: {e}")
        
    @staticmethod
    def save_encrypted_container(file_path, encrypted_data):
        try:
            with open(file_path, 'wb') as file:
                pickle.dump(encrypted_data, file)
            # print(f"Encrypted container successfully saved to {file_path}\n")
        except IOError as e:
            raise IOError(f"An error occurred while saving the encrypted container to {file_path}: {e}")
        
    @staticmethod
    def load_encrypted_container(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        try:
            with open(file_path, 'rb') as file:
                return pickle.load(file)
        except IOError as e:
            raise IOError(f"An error occurred while loading the encrypted container from {file_path}: {e}")