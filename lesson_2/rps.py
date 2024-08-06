import random
import os

WINNING_SCORE = 3
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

def wait_for_input():
    input("Press enter to continue:")
    clear_screen()

def clear_screen():
    os.system("clear")

def display_welcome_message():
    clear_screen()
    prompt(f"""Welcome to RPSLS.
Go to https://www.wikihow.com/Play-Rock-Paper-Scissors-Lizard-Spock for rules.
First to {WINNING_SCORE} wins will claim victory.""")

def display_goodbye_message():
    clear_screen()
    prompt("Thanks for playing RPSLS!")

def display_valid_choices():
    prompt(f"Choose one: {', '.join(VALID_CHOICES)} \
({', '.join(VALID_SHORTENED_CHOICES)})")

def display_choices(player, computer):
    clear_screen()
    prompt(f"You chose {player}, computer chose {computer}.")

def ask_play_again():
    prompt("Do you want to play again? (y/n)")

def display_winner(score):
    if score["player"] == WINNING_SCORE:
        prompt("Player won. Congratulations!")
    else:
        prompt("Computer won. Better luck next time!")

def determine_winner(player, computer):
    if computer in WINNING_COMBOS[player]:
        return "player"
    if player in WINNING_COMBOS[computer]:
        return "computer"

    return "tie"

def display_result(winner, score):
    if winner == "player":
        prompt("Player wins!")
    elif winner == "computer":
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

    prompt(f"Player: {score["player"]} - Computer: {score["computer"]}")
    wait_for_input()

def retrieve_player_choice():
    choice = input().strip().lower()

    while choice not in (VALID_CHOICES + VALID_SHORTENED_CHOICES):
        prompt("That's not a valid choice.")
        choice = input().strip().lower()

    if choice in VALID_SHORTENED_CHOICES:
        choice = VALID_CHOICES[VALID_SHORTENED_CHOICES.index(choice)]

    return choice

def retrieve_computer_choice():
    return random.choice(VALID_CHOICES)

def retrieve_yes_or_no():
    answer = input().strip().lower()

    while not valid_yes_or_no(answer):
        prompt("Please input a valid answer (y/n)")
        answer = input().strip().lower()

    clear_screen()
    return (answer in ['y', 'yes'])

def update_score(winner, score):
    if winner == "player":
        score["player"] += 1
    elif winner == "computer":
        score["computer"] += 1

def valid_yes_or_no(answer):
    return answer in ['y', 'yes', 'n', 'no']

def main():
    display_welcome_message()
    wait_for_input()

    while True:
        score = {"player": 0, "computer": 0}
        while max(score.values()) < WINNING_SCORE:
            display_valid_choices()
            player_choice = retrieve_player_choice()
            computer_choice = retrieve_computer_choice()

            display_choices(player_choice, computer_choice)

            winner = determine_winner(player_choice, computer_choice)
            update_score(winner, score)
            display_result(winner, score)

        display_winner(score)
        ask_play_again()
        play_again = retrieve_yes_or_no()

        if not play_again:
            break

    display_goodbye_message()

main()