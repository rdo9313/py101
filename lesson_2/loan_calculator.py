import json
import os

with open('loan_messages.json', 'r') as file:
    MSG = json.load(file)

MONTHS_IN_YEAR = 12

def prompt(msg):
    print(f"==> {msg}")

def clear_screen():
    os.system("clear")

def check_negative(num):
    return float(num) < 0

def display_welcome_message():
    clear_screen()
    prompt("""Welcome to Car Payment Calculator. We will calculate your
    monthly payment assuming that interest is compounded monthly. 
    Press any key to continue:""")

def display_monthly_payment(payment):
    prompt(f"Your monthly payment is ${payment:.2f}")

def display_goodbye_message():
    prompt("Thanks for using Car Payment Calculator!")

def wait_user_input():
    input()
    clear_screen()

def invalid_number(num):
    try:
        float(num)
    except ValueError:
        return True

    return False

def invalid_duration(months):
    try:
        int(months)
    except ValueError:
        return True

    return False

def invalid_input(string):
    return string.lower() in ['nan', 'inf']

def invalid_answer(answer):
    return answer not in ['y', 'yes', 'n', 'no']

def request_loan_amount():
    prompt("What is the total loan amount?")

def request_apr():
    prompt("What is the APR %? (i.e. 5.5, 12)")

def request_loan_duration():
    prompt("What is the loan duration (months)?")

def request_calculate_again():
    prompt("Would you like to calculate again for another loan? (y/n)")

def retrieve_value():
    number = input()

    while (invalid_number(number)
    or invalid_input(number)
    or check_negative(number)):
        prompt("Please enter a valid number:")
        number = input()

    return number

def retrieve_loan_duration():
    months = input()

    while invalid_duration(months) or check_negative(months):
        prompt("Please enter a non-negative whole number:")
        months = input()

    return months

def retrieve_answer():
    answer = input().lower()

    while invalid_answer(answer):
        prompt("Please input a valid answer:")
        answer = input().lower()

    clear_screen()
    return answer

def calculate_monthly_pmt(amount, apr, months):
    monthly_interest = float(apr) / MONTHS_IN_YEAR / 100

    if int(months) == 0:
        return float(amount)
    if monthly_interest == 0:
        return float(amount) / int(months)

    return float(amount) * (monthly_interest / (1 - (1 + monthly_interest)
           ** (-int(months))))


display_welcome_message()
wait_user_input()

while True:
    request_loan_amount()
    loan_amount = retrieve_value()

    request_apr()
    apr_amount = retrieve_value()

    request_loan_duration()
    loan_duration = retrieve_loan_duration()

    monthly_pmt = calculate_monthly_pmt(loan_amount, apr_amount, loan_duration)
    display_monthly_payment(monthly_pmt)

    request_calculate_again()
    calc_again = retrieve_answer()

    if calc_again in ['n', 'no']:
        break

display_goodbye_message()
