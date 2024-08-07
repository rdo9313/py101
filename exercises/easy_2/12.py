def negative(num):
    if num > 0:
        return -num
    
    return num

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True