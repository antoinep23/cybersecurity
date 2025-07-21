# 🛠️ Hash Brute Force Tool (Python)

A lightweight Python script that performs a dictionary-based brute-force attack to crack hashed passwords.  
Supports multiple hash algorithms and can automatically download the famous `rockyou.txt` wordlist if not provided.

## 🚀 Features

- Supports multiple hash algorithms: `md5`, `sha1`, `sha256`, `sha512`
- Accepts any custom wordlist or defaults to `rockyou.txt`
- Automatically downloads `rockyou.txt` if missing
- Clean CLI interaction and error handling

## 📦 Requirements

- Python 3.x
- `requests` module (`pip install requests`)

## 🔧 How It Works

1. User specifies:

   - The hash algorithm (e.g. `sha256`)
   - The path to the hash file
   - A custom wordlist (optional)

2. If no wordlist is specified, the script checks for `rockyou.txt`. If not found, it will automatically download it.

3. The script reads the target hash from the given file.

4. It then hashes every word in the wordlist using the selected algorithm and compares it to the target hash.

5. If a match is found, it prints the plaintext.

## 🖥️ Usage

```bash
$ python main.py
What is the hash type? (e.g. "sha256"): sha256
Enter the hash file location (e.g. hash.txt): hash.txt
Specify your wordlist (leave blank for the default rockyou.txt):
```

## ⚠️ Disclaimer

This tool is intended for educational and ethical purposes only.
Do not use it on any system, network, or data without explicit permission.

---

github.com/antoinep23
