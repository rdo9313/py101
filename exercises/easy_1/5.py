bill = float(input("What is the bill?"))
tip_percentage = float(input("What is the tip percentage?"))

tip = bill * tip_percentage / 100
total = bill + tip

print(f"The tip is ${tip:.2f}")
print(f"The total is ${total:.2f}")