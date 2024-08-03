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

def request_number(number):
    prompt(number)

def retrieve_number():
    number = input()

    while invalid_number(number) or number.lower() in ['nan', 'inf']:
        prompt("invalid_number")
        number = input()

    clear_screen()
    return number

def request_operation():
    prompt("choose_operation")

def retrieve_operation(num):
    operator = input()

    while operator == '4' and float(num) == 0:
        prompt("zero_division")
        operator = input()

    while operator not in ['1', '2', '3', '4']:
        prompt("invalid_operation")
        operator = input()

    return operator

def request_calculate_again():
    prompt("calculate_again")

def retrieve_answer():
    answer = input().lower()

    while invalid_answer(answer):
        prompt("invalid_answer")
        answer = input().lower()

    clear_screen()
    return answer

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

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def invalid_answer(answer):
    return answer not in ['y', 'yes', 'n', 'no']

clear_screen()
display_welcome_message()

while True:
    request_number("first_number")
    number1 = retrieve_number()

    request_number("second_number")
    number2 = retrieve_number()

    request_operation()
    operation = retrieve_operation(number2)

    result = calculate(operation, number1, number2)

    display_result(result, operation, number1, number2)

    request_calculate_again()
    calc_again = retrieve_answer()

    if calc_again in ['n', 'no']:
        break


display_goodbye_message()