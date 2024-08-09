import random
import os

SCORE = {"player": 0, "computer": 0}
WINNING_SCORE = 3
VALID_SHORTENED_CHOICES = ['r', 'p', 's', 'l', 'sp']
VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
CHOICE_DICT = {'r': 'rock', 'p': 'paper', 's': 'scissors',
               'l': 'lizard', 'sp': 'spock'}
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

def clear_screen(order = "next"):
    if order == "no_board":
        os.system("clear")
    else:
        os.system("clear")
        display_score()

def display_welcome_message():
    clear_screen("no_board")
    prompt(f"""Welcome to RPSLS.
Go to https://www.wikihow.com/Play-Rock-Paper-Scissors-Lizard-Spock for rules.
First to {WINNING_SCORE} wins will claim victory.""")

def display_goodbye_message():
    clear_screen("no_board")
    prompt("Thanks for playing RPSLS!")

def display_valid_choices():
    prompt(f"Choose one: {', '.join(VALID_CHOICES)} \
({', '.join(VALID_SHORTENED_CHOICES)})")

def display_choices(player, computer):
    clear_screen()
    prompt(f"You chose {player}, computer chose {computer}.")

def ask_play_again():
    prompt("Do you want to play again? (y/n)")

def display_winner():
    if SCORE["player"] == WINNING_SCORE:
        prompt("Player won. Congratulations!")
    else:
        prompt("Computer won. Better luck next time!")

def determine_winner(player, computer):
    if computer in WINNING_COMBOS[player]:
        return "player"
    if player in WINNING_COMBOS[computer]:
        return "computer"

    return "tie"

def display_score():
    prompt(f"Player: {SCORE["player"]}")
    prompt(f"Computer: {SCORE["computer"]}")

def display_result(winner):
    if winner == "player":
        prompt("Player wins!")
    elif winner == "computer":
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

    wait_for_input()

def reset_score():
    for key in SCORE:
        SCORE[key] = 0
    clear_screen()

def retrieve_player_choice():
    choice = input().strip().lower()

    while choice not in (VALID_CHOICES + VALID_SHORTENED_CHOICES):
        prompt("That's not a valid choice.")
        choice = input().strip().lower()

    if choice in VALID_SHORTENED_CHOICES:
        choice = CHOICE_DICT[choice]

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

def update_score(winner):
    if winner == "player":
        SCORE["player"] += 1
    elif winner == "computer":
        SCORE["computer"] += 1

def valid_yes_or_no(answer):
    return answer in ['y', 'yes', 'n', 'no']

def main():
    display_welcome_message()
    wait_for_input()

    while True:
        reset_score()
        while max(SCORE.values()) < WINNING_SCORE:
            display_valid_choices()
            player_choice = retrieve_player_choice()
            computer_choice = retrieve_computer_choice()

            winner = determine_winner(player_choice, computer_choice)
            update_score(winner)

            display_choices(player_choice, computer_choice)
            display_result(winner)

        display_winner()
        ask_play_again()
        play_again = retrieve_yes_or_no()

        if not play_again:
            break

    display_goodbye_message()

main()