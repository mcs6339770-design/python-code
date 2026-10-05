# Password Validation and Caesar Cipher Encryption

def check_password(password):
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True


def caesar_encrypt(text, shift=3):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


password = input("Enter password: ")

if check_password(password):
    encrypted = caesar_encrypt(password)

    with open("encrypted.txt", "w") as file:
        file.write(encrypted)

    print("Password is strong.")
    print("Encrypted password:", encrypted)
    print("Saved to encrypted.txt")
else:
    print("Password must contain:")
    print("- At least 8 characters")
    print("- Uppercase letter")
    print("- Lowercase letter")
    print("- Number")