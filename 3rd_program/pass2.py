# Password Validation and XOR Encryption

def validate_password(password):
    return (
        len(password) >= 8
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
    )


def xor_encrypt(text, key):
    encrypted = ""

    for char in text:
        encrypted += chr(ord(char) ^ key)

    return encrypted


password = input("Enter password: ")

if validate_password(password):
    key = 7
    encrypted = xor_encrypt(password, key)

    with open("encrypted.txt", "w", encoding="utf-8") as file:
        file.write(encrypted)

    print("Password is strong.")
    print("Encrypted data saved successfully.")
else:
    print("Weak password!")
    print("Use at least 8 characters with uppercase, lowercase and numbers.")