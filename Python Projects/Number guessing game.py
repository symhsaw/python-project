import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Choose your difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    # Get difficulty level from the user
    while True:
        try:
            difficulty = int(input("Enter the difficulty level (1/2/3): "))
            if difficulty not in [1, 2, 3]:
                raise ValueError("Invalid choice. Please select 1, 2, or 3.")
            break
        except ValueError as e:
            print(e)

    # Set range based on difficulty level
    if difficulty == 1:
        max_number = 10
    elif difficulty == 2:
        max_number = 50
    else:
        max_number = 100

    # Generate random number to guess
    number_to_guess = random.randint(1, max_number)
    attempts = 0

    print(f"I have selected a number between 1 and {max_number}. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > max_number:
                print(f"Please enter a number between 1 and {max_number}.")
                continue

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
