import hashlib
import requests


# Get the hash type from the user
hash_type = input('What is the hash type? (e.g. "sha256"): ').strip().lower()
if not hash_type:
    print("Invalid input for hash type.")
    exit()

# Get the file location
file_location = input("Enter the hash file location (e.g. hash.txt): ").strip()
if not file_location:
    print("Invalid input for file location.")
    exit()

# Get the user's custom wordlist
specified_wordlist = input("Specify your wordlist (leave blank for the default rockyou.txt): ") or "rockyou.txt"

if specified_wordlist == "rockyou.txt":
    # Check if rockyou.txt exists, if not, download it
    try:
        with open("rockyou.txt", 'r', encoding='utf-8') as file:
            print("Using existing rockyou.txt wordlist.")
    except FileNotFoundError:
        try:
            print("rockyou.txt not found. Downloading...")

            rockyou_url = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
            response = requests.get(rockyou_url)
            response.raise_for_status()  # Check for HTTP errors

            with open("rockyou.txt", 'w', encoding='utf-8') as file:
                file.write(response.text)

            print("rockyou.txt downloaded successfully.")
        except requests.RequestException as e:
            print(f"Failed to download rockyou.txt: {e}")
            exit()

# Define the wordlist
try:
    with open(specified_wordlist, 'r', encoding='utf-8') as file:
        wordlist = file.read().splitlines()
except FileNotFoundError:
    print("Wordlist not found.")
    exit()

print("Starting brute force... 🔓")

# Read the target hash from the file once
try:
    with open(file_location, 'r') as file:
            target_hash = file.read().strip()
except FileNotFoundError:
    print("Hash file not found.")
    exit()

match_found = False

# Iterate through each word in the wordlist
for word in wordlist:
    # Create the hash of the word
    if hash_type == 'md5':
        hash_object = hashlib.md5(word.encode())
    elif hash_type == 'sha1':
        hash_object = hashlib.sha1(word.encode())
    elif hash_type == 'sha256':
        hash_object = hashlib.sha256(word.encode())
    elif hash_type == 'sha512':
        hash_object = hashlib.sha512(word.encode())
    else:
        print("Unsupported hash type.")
        exit()

    # Get the hexadecimal digest of the hash
    hashed_word = hash_object.hexdigest()

    # Check if the hashed word matches the target hash
    if hashed_word == target_hash:
        print(f"✅ Match found: {word} -> {hashed_word}")
        match_found = True
        break

if not match_found:
    print("❌ No match found in the wordlist.")
