# Password Validation and Base64 Encoding

import base64


def password_strength(password):
    if len(password) < 8:
        return False

    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)

    return upper and lower and digit


password = input("Enter password: ")

if password_strength(password):

    encoded = base64.b64encode(
        password.encode()
    ).decode()

    with open("encrypted.txt", "w") as file:
        file.write(encoded)

    print("Password accepted.")
    print("Encoded password:", encoded)
    print("Data stored in encrypted.txt")

else:
    print("Password is weak.")
    print("Password should contain uppercase, lowercase and numbers.")