import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_punctuation=True):
    # Define the character sets based on user preferences
    all_chars = ''
    if use_lowercase:
        all_chars += string.ascii_lowercase
    if use_uppercase:
        all_chars += string.ascii_uppercase
    if use_digits:
        all_chars += string.digits
    if use_punctuation:
        all_chars += string.punctuation

    # Check if any character set is selected
    if not all_chars:
        raise ValueError("At least one character set should be selected.")

    # Generate a random password of specified length
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Example usage:
length = int(input("Enter the length of the password: "))
lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
digits = input("Include digits? (yes/no): ").lower() == 'yes'
punctuation = input("Include punctuation? (yes/no): ").lower() == 'yes'

try:
    password = generate_password(length, lowercase, uppercase, digits, punctuation)
    print("Generated Password:", password)
except ValueError as e:
    print("Error:", e)
