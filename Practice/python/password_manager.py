import hashlib
from cryptography.fernet import Fernet
import json
import os

KEY_FILE = 'key.key'
PASSWORD_FILE = 'passwords.json'

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as file:
            file.write(key)
    else:
        with open(KEY_FILE, 'rb') as file:
            key = file.read()
    return key

def encrypt_password(password, fernet):
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(enc_password, fernet):
    return fernet.decrypt(enc_password.encode()).decode()

def add_password(account, username, password):
    key = load_key()
    fernet = Fernet(key)

    data = {}
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as file:
            data = json.load(file)

    data[account] = {
        'username': username,
        'password': encrypt_password(password, fernet)
    }

    with open(PASSWORD_FILE, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Password for '{account}' saved successfully.")

def retrieve_password(account):
    key = load_key()
    fernet = Fernet(key)

    if not os.path.exists(PASSWORD_FILE):
        print("No passwords stored yet.")
        return

    with open(PASSWORD_FILE, 'r') as file:
        data = json.load(file)

    if account in data:
        username = data[account]['username']
        password = decrypt_password(data[account]['password'], fernet)
        print(f"Account: {account}\nUsername: {username}\nPassword: {password}")
    else:
        print(f"No details found for '{account}'.")

if __name__ == "__main__":
    while True:
        action = input("Choose action [add/retrieve/exit]: ").lower()
        if action == 'add':
            account = input("Account: ")
            username = input("Username: ")
            password = input("Password: ")
            add_password(account, username, password)
        elif action == 'retrieve':
            account = input("Account: ")
            retrieve_password(account)
        elif action == 'exit':
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid action, try again.")
