import datetime

age = int(input("What is your age?"))
retirement_age = int(input("At what age would you like to retire?"))
current_year = datetime.datetime.now().year
years_left = retirement_age - age

print(f"It's {current_year}. You will retire in {current_year + years_left}.")
print(f"You have only {years_left} years of work to go!")