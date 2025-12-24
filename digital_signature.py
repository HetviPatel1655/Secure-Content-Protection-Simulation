# Task 3: Secure Signature and Verification
# Implement a module for generating and validating digital signatures using the RSA-PSS padding scheme with SHA-256.
# Requirements: Demonstrate that verify_signature successfully rejects the signature if the input data or the signature itself is tampered with.

from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256

def sign_data(data_bytes, rsa_private_key):
    rsa_private_key = RSA.import_key(rsa_private_key)
    h = SHA256.new(data_bytes)
    signature = ((pss.new(rsa_private_key)).sign(h))
    return signature

def verify_signature(data_bytes, signature, rsa_public_key):
    h = SHA256.new(data_bytes)
    rsa_public_key = RSA.import_key(rsa_public_key)
    verifier = pss.new(rsa_public_key)
    try:
        verifier.verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False
    