integer = int(input("Please enter an integer greater than 0:"))
operation = input("Enter 's' to computer the sum, or 'p' to compute the product.")

sum = sum(range(integer + 1))

product = 1
for num in range(1, integer + 1):
    product *= num

if operation == 's':
    print(f"The sum of the integers between 1 and {integer} is {sum}.")
if operation == 'p':
    print(f"The product of the integers between 1 and {integer} is {product}.")