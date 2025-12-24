# Secure-Content-Protection-Simulation# Secure-Content-Protection-Simulation
# Secure Content Protection Simulation

This repository contains an ongoing internship project focused on implementing core cryptography and Digital Rights Management (DRM) fundamentals using Python and the PyCryptodome library.

The project is designed as a **learning-oriented simulation** and does not claim to be a production-ready DRM system.

---

## Implemented Cryptography Concepts

- Symmetric vs Asymmetric Encryption
- AES Encryption Modes:
  - CBC
  - CTR
  - CFB
  - OFB
  - GCM
- Initialization Vectors (IVs) and Nonces
- PKCS#7 Padding
- Hybrid Encryption:
  - AES-256-GCM for content encryption
  - RSA-OAEP for AES key wrapping
- Digital Signatures:
  - RSA-PSS with SHA-256
  - Tamper detection for data and signatures

---

## Project Structure
secure-content-protection-simulation/
│
├── aes_engine.py # AES encryption/decryption implementations
├── hybrid_encryption.py # Hybrid encryption (AES + RSA)
├── digital_signature.py # RSA-PSS digital signatures
├── demo.py # Demonstration script
├── sample.txt # Sample input file
├── README.md
└── .gitignore


---

## How to Run

1. Create and activate a virtual environment
2. Install dependencies:
   ```bash
   pip install pycryptodome
3. Run the Demo
   python demo.py
4. Select the encryption mode and input file when prompted

Limitations :
This project is intended for educational and internship learning purposes No license server, access policy enforcement, or secure key storage Not intended for production DRM usage
