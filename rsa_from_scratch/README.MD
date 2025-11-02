# RSA Implementation

A basic implementation of the RSA cryptographic algorithm in Python.

## Overview

This implementation provides the core RSA functionality including:

- Key generation with user-defined prime numbers
- Message encryption using the public key
- Message decryption using the private key

### Key Generation

- Uses two prime numbers `p` and `q` to compute the modulus: n = p \* q

- Calculates Euler's totient function: φ(n) = (p - 1) \* (q - 1)

- Uses a fixed public exponent `e = 65537` (a common choice in RSA)

- Computes the private exponent `d` using the modular inverse: d = e^-1 mod φ(n)

### 🔐 Encryption / 🔓 Decryption

- Messages are:

  - Encoded to UTF-8 bytes
  - Converted to integers for computation

- **Encryption**: c = m^e mod n

- **Decryption**: m = c^d mod n

- Results are decoded back into UTF-8 strings

---

## ⚠️ Important Limitations

> **This implementation is for educational purposes only and lacks critical security features.**

- ❌ **No padding scheme**  
  (e.g. PKCS#1 v1.5 — necessary for real-world security)

- ❌ **Message size limitations**  
  Messages must be smaller than the modulus `n`

- ❌ **No random prime generation**  
  Requires manual input of prime numbers

- ❌ **Basic error handling**  
  Limited validation and error reporting

---

## Usage

```python
# Generate keys with two prime numbers
keys = generate_rsa_keys(p=22079, q=22091)

# Encrypt a message
ciphertext = rsa_encrypt("Hello World", keys["public_key"])

# Decrypt the message
plaintext = rsa_decrypt(ciphertext, keys["private_key"])
```

---

github.com/antoinep23
