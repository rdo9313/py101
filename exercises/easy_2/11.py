def center_of(str):
    center = len(str) // 2
    if len(str) % 2 == 1:
        return str[center]
    
    return str[center - 1: center + 1]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True