import random

VALID_SHORTENED_CHOICES = ['r', 'p', 's', 'l', 'sp']
VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
WINNING_COMBOS = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "spock": ["rock", "scissors"],
    "lizard": ["spock", "paper"]
}

def prompt(message):
    print(f"==> {message}")

def display_welcome_message():
    prompt(f"""Welcome to RPSLS. 
Go to https://www.wikihow.com/Play-Rock-Paper-Scissors-Lizard-Spock for rules.
Press any key to continue:""")

def determine_winner(player, computer):
    if computer in WINNING_COMBOS[player]:
        return player
    elif player in WINNING_COMBOS[computer]:
        return computer
    else:
        return "tie"

def display_winner(player, computer):
    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")):
        prompt("You win!")
    elif ((player == "rock" and computer == "paper") or
        (player == "paper" and computer == "scissors") or
        (player == "scissors" and computer == "rock")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

def retrieve_player_choice():
    choice = input().strip().lower()

    while choice not in (VALID_CHOICES or VALID_SHORTENED_CHOICES):
        prompt("That's not a valid choice.")
        choice = input().strip().lower()
    
    return choice

def retrieve_computer_choice():
    return random.choice(VALID_CHOICES)

display_welcome_message()

while True:
    prompt(f"Choose one: {', '.join(VALID_CHOICES)} ({', '.join(VALID_SHORTENED_CHOICES)})")
    choice = retrieve_player_choice()

    computer_choice = retrieve_computer_choice()

    prompt(f"You chose {choice}, computer chose {computer_choice}")

    display_winner(choice, computer_choice)

    prompt("Do you want to play again? (y/n)")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt("Please enter 'y' or 'n'.")
        answer = input().lower()
    
    if answer[0] == 'n':
        break