import json
import os

with open('loan_messages.json', 'r') as file:
    MSG = json.load(file)

def prompt(msg):
    print(f"==> {msg}")


os.system('clear')
prompt("""Welcome to Car Payment Calculator. We will calculate your monthly payment 
assuming that interest is compounded monthly. Press any key to continue:""")
input()

while True:
    prompt("What is the total loan amount?")
    loan_amount = float(input())

    prompt("What is the APR %?")
    apr_amount = float(input())
    monthly_interest = apr_amount / 12 / 100

    prompt("What is the loan duration (months)?")
    loan_duration = int(input())

    monthly_payment = loan_amount * (monthly_interest / (1 - (1 + monthly_interest) ** (-loan_duration)))

    prompt(f"Your monthly payment is ${monthly_payment:.2f}")

    prompt("Would you like to calculate monthly payments for another loan?")
    answer = input()

    if answer == 'n':
        break

prompt("Thanks for using Car Payment Calculator!")

