# Secure Password Validation using SHA-256 Hashing

import hashlib


def validate_password(password):
    conditions = [
        len(password) >= 8,
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(not c.isalnum() for c in password)
    ]

    return all(conditions)


def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


password = input("Enter password: ")

if validate_password(password):

    hashed_password = hash_password(password)

    with open("password_hash.txt", "w") as file:
        file.write(hashed_password)

    print("Password is strong.")
    print("SHA-256 hash:", hashed_password)
    print("Hash saved successfully.")

else:
    print("Weak password!")
    print("Password must contain:")
    print("1. At least 8 characters")
    print("2. Uppercase letter")
    print("3. Lowercase letter")
    print("4. Number")
    print("5. Special character")