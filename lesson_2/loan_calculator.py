import json
import os

with open('loan_messages.json', 'r') as file:
    MSG = json.load(file)

MONTHS_IN_YEAR = 12

def prompt(msg):
    try:
        MSG[msg]
    except KeyError:
        print(f"==> {msg}")
    else:
        print(f"==> {MSG[msg]}")

def clear_screen():
    os.system("clear")

def line_break():
    prompt("-----------------------------------------------")

def is_zero_or_positive(num):
    return float(num) >= 0

def is_positive(num):
    return float(num) > 0

def valid_loan_decimal(loan):
    return is_integer(loan) or len(loan.rsplit('.')[-1]) <= 2

def display_welcome_message():
    clear_screen()
    prompt("welcome_message")

def display_monthly_pmt(loan_amt, apr, months, payment):
    clear_screen()
    line_break()
    prompt(f"Your loan amount is ${float(loan_amt):.2f}.")
    prompt(f"Your APR is {apr}%.")
    prompt(f"Your loan duration is {months} months.")
    line_break()
    prompt(f"Your monthly payment is ${payment:.2f}.")
    line_break()

def display_goodbye_message():
    prompt("goodbye_message")

def wait_user_input():
    input()
    clear_screen()

def is_float(num):
    try:
        float(num)
    except ValueError:
        return False

    return True

def is_integer(months):
    try:
        int(months)
    except ValueError:
        return False

    return True

def nan_or_inf(string):
    return string.lower() in ['nan', 'inf']

def valid_yes_or_no(answer):
    return answer in ['y', 'yes', 'n', 'no']

def validate_loan(number):
    while nan_or_inf(number) or not \
    (is_float(number)
    and is_positive(number)
    and valid_loan_decimal(number)):
        prompt("valid_loan")
        number = input().strip()

    return number

def validate_apr(number):
    while nan_or_inf(number) or not \
    (is_float(number) and is_zero_or_positive(number)):
        prompt("valid_apr")
        number = input().strip()

    return number

def validate_loan_duration(number):
    while not (is_integer(number) and is_positive(number)):
        prompt("valid_loan_duration")
        number = input().strip()

    return number

def retrieve_value(input_type):
    value = input().strip()

    match input_type:
        case "loan":
            return validate_loan(value)
        case "apr":
            return validate_apr(value)
        case "loan_duration":
            return validate_loan_duration(value)
        case _:
            pass

def retrieve_yes_or_no():
    answer = input().strip().lower()

    while not valid_yes_or_no(answer):
        prompt("valid_answer")
        answer = input().strip().lower()

    clear_screen()
    return (answer in ['y', 'yes'])

def calculate_monthly_pmt(amount, apr, months):
    monthly_interest = float(apr) / MONTHS_IN_YEAR / 100

    if int(months) == 0:
        return float(amount)
    if monthly_interest == 0:
        return float(amount) / int(months)

    return float(amount) * (monthly_interest / (1 - (1 + monthly_interest)
           ** (-int(months))))

def main():
    display_welcome_message()
    wait_user_input()

    while True:
        prompt("loan")
        loan = retrieve_value("loan")

        prompt("apr")
        apr_amount = retrieve_value("apr")

        prompt("loan_duration")
        loan_duration = retrieve_value("loan_duration")

        monthly_pmt = calculate_monthly_pmt(loan, apr_amount, loan_duration)
        display_monthly_pmt(loan, apr_amount, loan_duration, monthly_pmt)

        prompt("calculate_again")
        calc_again = retrieve_yes_or_no()

        if not calc_again:
            break

    display_goodbye_message()

main()