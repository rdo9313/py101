def xor(a, b):
    return (bool(a) == True and bool(b)) == False or (bool(b) == True and bool(a) == False)


print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)