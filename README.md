# 🔐 Password Audit

A simple but professional **Password Audit** script.  
It checks the security of a given password, supports different input methods, and saves the result to a file.

---

## 🚀 Features
- Checks for lowercase, uppercase, digits, and special characters
- Supports CLI (command line) and interactive input
- Secure password entry with `getpass`
- Automatically saves results to a file (`password_audit.txt`)

---

## 📦 Libraries Used
- `re` → Regex for password validation  
- `argparse` → Command-line argument parsing  
- `pathlib` → File handling  
- `sys` → Command-line control  
- `getpass` → Secure hidden password input  

---

## ⚡ Usage

### 1. Run normally
```bash
python password_audit.py
```
## Pass password via CLI
python password_audit.py MyPassword123!

## Hidden input (getpass)
python password_audit.py
Enter your password: ****
## 📝 Output
Enter Password: MyPassword123!
Valid Password
Password saved to /.../password_audit.txt

## 📌 Note
This script is for educational purposes only.
In real-world applications, never store passwords in plain text files.
