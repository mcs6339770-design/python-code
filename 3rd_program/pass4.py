# Password Validation and Character Shift Encryption

def validate(password):
    has_upper = False
    has_lower = False
    has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    return len(password) >= 8 and has_upper and has_lower and has_digit


def encrypt(password):
    encrypted = ""

    for ch in password:
        encrypted += chr(ord(ch) + 5)

    return encrypted


password = input("Enter your password: ")

if validate(password):
    encrypted_password = encrypt(password)

    file = open("password.txt", "w")
    file.write(encrypted_password)
    file.close()

    print("Password validation successful.")
    print("Encrypted password:", encrypted_password)
    print("Stored in password.txt")

else:
    print("Invalid password.")
    print("Password requires 8+ characters, uppercase, lowercase and number.")