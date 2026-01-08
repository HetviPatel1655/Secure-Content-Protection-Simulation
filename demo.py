# Separate the audio-video file from the audio-video container using any Python library 
# Extract the byte array of the video file

import os
import media_demux_ffmpeg_cli
from aes_engine import *
from hybrid_encryption import *
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from digital_signature import *
import time

print("\nAES Encryption/Decryption Demo with Multiple Modes")

video_files = ['Test Video 10MB.mp4', 'Test Video 25MB.mp4',  'Test Video 50MB.mp4', 'Test Video 100MB.mp4']
# Change index to test different sizes
for file_data in video_files:
    print("\n" + "="*100)
    print("\nFile size(in mb):", os.path.getsize(file_data)/(1024*1024))
    print(f"\nProcessing file of size: {os.path.getsize(file_data)} bytes")

    video_stream, audio_stream = media_demux_ffmpeg_cli.extract_streams(file_data, 'video_output.h264', 'audio_output.aac')
# if (mode == 1):
    print("\n--------------------CBC Mode Selected--------------------")
    start_time = time.time()

    # Encryption Video Streams
    key_video = get_random_bytes(16) # AES-128
    encrypted_video_stream, iv_video = aes_encrypt_cbc(video_stream, key_video)
    # Encryption Audio Streams
    key_audio = get_random_bytes(16) # AES-128
    encrypted_audio_stream, iv_audio = aes_encrypt_cbc(audio_stream, key_audio)
    end_time = time.time()
    print(f"CBC Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")

    start_time = time.time()
    decrypted_video_stream = aes_decrypt_cbc(encrypted_video_stream, iv_video, key_video)
    decrypted_audio_stream = aes_decrypt_cbc(encrypted_audio_stream, iv_audio, key_audio)
    end_time = time.time()
    print(f"CBC Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")
    
# #elif (mode) == 2:
    print("\n--------------------CTR Mode Selected--------------------")
    start_time = time.time()
    key_video = get_random_bytes(16) 
    encrypyted_video_stream, nonce_video = aes_encrypt_ctr(video_stream, key_video)
    key_audio = get_random_bytes(16) 
    encrypyted_audio_stream, nonce_audio = aes_encrypt_ctr(audio_stream, key_audio)
    end_time = time.time()
    print(f"CTR Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
    start_time = time.time()
    decrypted_video_stream = aes_decrypt_ctr(encrypyted_video_stream, nonce_video, key_video)
    decrypted_audio_stream = aes_decrypt_ctr(encrypyted_audio_stream, nonce_audio, key_audio)
    end_time = time.time()
    print(f"CTR Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")
# #elif (mode) == 3:
    print("\n--------------------CFB Mode Selected--------------------")
    start_time = time.time()
    key_video = get_random_bytes(16) 
    encrypted_video_stream, iv_video = aes_encrypt_cfb(video_stream, key_video)
    key_audio = get_random_bytes(16)
    encrypted_audio_stream, iv_audio     = aes_encrypt_cfb(audio_stream, key_audio)
    end_time = time.time()
    print(f"CFB Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
    start_time = time.time()
    decrypted_video_stream = aes_decrypt_cfb(encrypted_video_stream, iv_video, key_video)
    decrypted_audio_stream = aes_decrypt_cfb(encrypted_audio_stream, iv_audio, key_audio)
    end_time = time.time()
    print(f"CFB Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")
# #elif (mode) == 4:
    print("\n--------------------OFB Mode Selected--------------------")
    start_time = time.time()
    key_video = get_random_bytes(16) 
    encrypted_video_stream, iv_video = aes_encrypt_ofb(video_stream, key_video)
    key_audio = get_random_bytes(16)
    encrypted_audio_stream, iv_audio = aes_encrypt_ofb(audio_stream, key_audio)
    end_time = time.time()
    print(f"OFB Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
    start_time = time.time()
    decrypted_video_stream = aes_decrypt_ofb(encrypted_video_stream, iv_video, key_video)
    decrypted_audio_stream = aes_decrypt_ofb(encrypted_audio_stream, iv_audio, key_audio)
    end_time = time.time()
    print(f"OFB Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")
# #elif (mode) == 5:
    print("\n--------------------GCM Mode Selected--------------------")
    start_time = time.time()
    key_video = get_random_bytes(16) 
    encrypted_video_stream, nonce_video, tag_video = aes_encrypt_gcm(video_stream, key_video)
    key_audio = get_random_bytes(16)
    encrypted_audio_stream, nonce_audio, tag_audio = aes_encrypt_gcm(audio_stream, key_audio)
    end_time = time.time()
    print(f"GCM Mode Time Taken for Encryption: {end_time - start_time:.4f} seconds")
    start_time = time.time()
    decrypted_video_stream = aes_decrypt_gcm(encrypted_video_stream, nonce_video, key_video, tag_video)
    decrypted_audio_stream = aes_decrypt_gcm(encrypted_audio_stream, nonce_audio, key_audio, tag_audio)
    end_time = time.time()
    print(f"GCM Mode Time Taken for Decryption: {end_time - start_time:.4f} seconds")
# #elif (mode) == 6:
    print("\n--------------------Hybrid Encryption Selected--------------")
    start_time = time.time()
    rsa_key_video = RSA.generate(2048)
    private_key_video = rsa_key_video.export_key()
    public_key_video = rsa_key_video.publickey().export_key()
    encrypted_video_stream = encrypt_content(video_stream, public_key_video)

    rsa_key_audio = RSA.generate(2048)
    private_key_audio = rsa_key_audio.export_key()
    public_key_audio = rsa_key_audio.publickey().export_key()
    encrypted_audio_stream = encrypt_content(audio_stream, public_key_audio)

    end_time = time.time()
    print(f"Hybrid Encryption Time Taken: {end_time - start_time:.4f} seconds")

    start_time = time.time()
    decrypted_video_stream = decrypt_content(encrypted_video_stream, private_key_video)
    decrypted_audio_stream = decrypt_content(encrypted_audio_stream, private_key_audio)
    end_time = time.time()
    print(f"Hybrid Decryption Time Taken: {end_time - start_time:.4f} seconds")

    print("\n------------------------------End of Processing for this file -------------------------------")



# Demonstration of Digital Signature and Verification
# Separate RSA keys used for encryption and signing (recommended practice)

print("\nDigital Signature and Verification Demo\n")
rsa_key = RSA.generate(2048)
private_key = rsa_key.export_key()
public_key = rsa_key.publickey().export_key()

# Sign the data
signature = sign_data(video_stream, private_key)
print("Signature generated.")

# Verify the signature (should be valid)
is_valid = verify_signature(video_stream, signature, public_key)
print(f"Signature valid: {is_valid}")

# Tamper with the data
tampered_data = video_stream[:-1] + bytes([video_stream[-1] ^ 0x01])  # Flip last bit
# Verify the signature with tampered data (should be invalid)
is_valid_tampered = verify_signature(tampered_data, signature, public_key)
print(f"Signature valid after tampering with data: {is_valid_tampered}")

# Tamper with the signature
tampered_signature = signature[:-1] + bytes([signature[-1] ^ 0x01])  # Flip last bit

# Verify the tampered signature (should be invalid)
is_valid_tampered_sig = verify_signature(video_stream, tampered_signature, public_key)
print(f"Signature valid after tampering with signature: {is_valid_tampered_sig}")
