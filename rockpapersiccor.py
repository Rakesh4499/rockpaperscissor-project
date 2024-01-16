import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def print_choices(user_choice, computer_choice):
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

# Initialize scores
user_score = 0
computer_score = 0

while True:
    print("\nRock, Paper, Scissors Game")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    # Get user input for choice
    user_choice_num = input("Enter your choice (1, 2, 3, or 4): ")

    if user_choice_num == '4':
        print("Thanks for playing! Final Scores:")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")
        break

    try:
        user_choice_num = int(user_choice_num)
        if user_choice_num not in [1, 2, 3]:
            print("Invalid choice. Please enter a valid option.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    choices = ["rock", "paper", "scissors"]
    user_choice = choices[user_choice_num - 1]
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)
    print_choices(user_choice, computer_choice)
    print(result)

    # Update scores
    if "win" in result:
        user_score += 1
    elif "lose" in result:
        computer_score += 1

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Final Scores:")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")
        break