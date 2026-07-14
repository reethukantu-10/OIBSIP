import random
import string


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase

    if use_lower:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("=" * 45)
print("      RANDOM PASSWORD GENERATOR")
print("=" * 45)

while True:

    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password must be at least 8 characters long.\n")
            continue

    except ValueError:
        print("Please enter a valid number.\n")
        continue

    print("\nChoose character types (yes/no)")

    upper = input("Include Uppercase Letters? ").strip().lower() == "yes"
    lower = input("Include Lowercase Letters? ").strip().lower() == "yes"
    digits = input("Include Numbers? ").strip().lower() == "yes"
    symbols = input("Include Symbols? ").strip().lower() == "yes"

    selected = sum([upper, lower, digits, symbols])

    if selected < 2:
        print("\nPlease select at least TWO character types.\n")
        continue

    password = generate_password(length, upper, lower, digits, symbols)

    print("\nGenerated Password")
    print("-" * 25)
    print(password)
    print("-" * 25)

    again = input("\nGenerate another password? (yes/no): ").strip().lower()

    if again != "yes":
        print("\nThank you for using the Password Generator!")
        break