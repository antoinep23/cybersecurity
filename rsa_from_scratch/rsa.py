import math


def generate_rsa_keys(p, q):
    # Calculate the shared modulo n
    n = p * q
    
    # Calculate φ(n)
    phi_n = (p - 1) * (q - 1)

    # Define the public exposant e
    e = 65537
    if math.gcd(e, phi_n) != 1:
        raise ValueError("e and phi(n) are not prime each")

    # Calculate the private exposant d
    d = pow(e, -1, phi_n)

    return {
        "public_key": (e, n),
        "private_key": (d, n),
        "n": n,
        "phi_n": phi_n
    }


def rsa_encrypt(message, public_key):
    e, n = public_key

    # Encode the message
    message_bytes = message.encode("utf-8")

    # Convert to integer
    m = int.from_bytes(message_bytes, byteorder="big")

    # Check if the message is not too big
    if m >= n:
        raise ValueError("Message too big for the key")

    # Encrypt the message
    c = pow(m, e, n)
    return c

def rsa_decrypt(ciphertext, private_key):
    d, n = private_key

    # Decrypt the ciphertext
    decrypted_m = pow(ciphertext, d, n)

    # Convert to bytes
    if decrypted_m == 0:
        decrypted_bytes = b'\x00'
    else:
        # Calcul the required number of bytes
        byte_length = (decrypted_m.bit_length() + 7) // 8
        decrypted_bytes = decrypted_m.to_bytes(byte_length, byteorder='big')

    # Decode the message
    return decrypted_bytes.decode("utf-8")
    

#############################
########## TEST #############
#############################

if __name__ == "__main__":
    # RSA parameters
    p = 22079
    q = 22091
    
    print("=== RSA test ===")
    print(f"p = {p}, q = {q}")
    print()
    
    message = "Hi"
    print("👉 Original message:", message)

    keys = generate_rsa_keys(p, q)
    print("🔑 Key generated", keys)

    cyphertext = rsa_encrypt(message, keys["public_key"])
    print("🔐 Encrypted message:", cyphertext)

    m = rsa_decrypt(cyphertext, keys["private_key"])
    print("🔓 Decrypted message:", m)
