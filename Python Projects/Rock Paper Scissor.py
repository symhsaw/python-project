import random

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions: Enter 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit the game.")

    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Your choice: ").strip().lower()

        if user_choice == 'quit':
            print("Thanks for playing!")
            print(f"Final Score: You: {user_score}, Computer: {computer_score}")
            break

        if user_choice not in choices:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Current Score: You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    rock_paper_scissors()
