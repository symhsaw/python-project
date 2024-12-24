import random
import string

def password_generator():
    print("Welcome to the Password Generator!")

    # Get password length from user
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 6): "))
            if length < 6:
                print("Password length must be at least 6 characters. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get user preferences
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    include_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"

    # Build character pool based on preferences
    character_pool = string.ascii_lowercase
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_numbers:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation

    # Ensure the character pool is not empty
    if not character_pool:
        print("You must select at least one character type. Please restart the program.")
        return

    # Generate password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    print(f"Your generated password is: {password}")

# Run the program
if __name__ == "__main__":
    password_generator()
