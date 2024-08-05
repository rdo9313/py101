import json
import os

with open('calculator_messages.json', 'r') as file:
    MSG = json.load(file)

LANGUAGE = "en"
operations= {
    "1": "+",
    "2": "-",
    "3": "*",
    "4": "/"
}

def messages(message, lang = "en"):
    return MSG[lang][message]

def prompt(msg):
    try:
        messages(msg, LANGUAGE)
    except KeyError:
        print(f"==> {msg}")
    else:
        message = messages(msg, LANGUAGE)
        print(f"==> {message}")

def clear_screen():
    os.system('clear')

def display_welcome_message():
    prompt("welcome")

def display_goodbye_message():
    prompt("goodbye")

def display_result(calculation, operator, num1, num2):
    prompt(f"{num1} {operations[operator]} {num2} = {calculation}")

def request_first_number():
    prompt("first_number")

def request_second_number():
    prompt("second_number")

def retrieve_number():
    number = input().strip()

    while not valid_number(number) or (number.lower() in ['nan', 'inf']):
        prompt("invalid_number")
        number = input().strip()

    clear_screen()
    return number

def request_operation():
    prompt("choose_operation")

def retrieve_operation(num):
    operator = input().strip()

    while operator == '4' and float(num) == 0:
        prompt("zero_division")
        operator = input().strip()

    while operator not in ['1', '2', '3', '4']:
        prompt("invalid_operation")
        operator = input().strip()

    return operator

def request_calculate_again():
    prompt("calculate_again")

def retrieve_yes_or_no():
    answer = input().strip().lower()

    while not valid_yes_or_no(answer):
        prompt("invalid_answer")
        answer = input().strip().lower()

    clear_screen()
    return (answer in ['y', 'yes'])

def calculate(operator, first_num, second_num):
    num1 = float(first_num)
    num2 = float(second_num)

    match operator:
        case '1':
            output = num1 + num2
        case '2':
            output = num1 - num2
        case '3':
            output = num1 * num2
        case '4':
            output = num1 / num2

    return round(output, 2)

def valid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return False

    return True

def valid_yes_or_no(answer):
    return answer in ['y', 'yes', 'n', 'no']

clear_screen()
display_welcome_message()

def main():
    while True:
        request_first_number()
        number1 = retrieve_number()

        request_second_number()
        number2 = retrieve_number()

        request_operation()
        operation = retrieve_operation(number2)

        result = calculate(operation, number1, number2)

        display_result(result, operation, number1, number2)

        request_calculate_again()
        calc_again = retrieve_yes_or_no()

        if not calc_again:
            break


    display_goodbye_message()

main()