import random

play_again = "yes" 

print("WELCOME TO THE ROUGH PAPER SCISSORS GAME!!!!")
while play_again == 'yes':
    user_response = input("Do you want to play the game? yes/no: ").lower()
    if user_response == "yes":
        print("Okay, let's start the game. Best wishes!")
    else:
        print("Okay, see you next time.")

    while True:
        user_input = input("Enter your choice: rock/paper/scissors: ").lower()
        options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(options)

        if user_input not in options:
            print("Please enter the valid option.")
        elif (user_input == 'rock' and computer_choice == 'scissors') or \
                (user_input == 'paper' and computer_choice == 'rock') or \
                (user_input == 'scissors' and computer_choice == 'paper'):
            print(f"computer's choice:{computer_choice}")
            print("YAY! YOU WON THE GAME")
        elif user_input == computer_choice:
            print("Oh great! It's a tie.")
        else:
            print("Computer won... Keep on trying.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

print("Thanks for playing! Goodbye!")
