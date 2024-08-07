def print_in_box(str):
    border = "+" + "-" * (len(str) + 2) + "+"
    empty_space = "|" + " " * (len(str) + 2) + "|"
    print(border)
    print(empty_space)
    print(f"| {str} |")
    print(empty_space)
    print(border)


print_in_box('To boldly go where no one has gone before.')
print_in_box('')