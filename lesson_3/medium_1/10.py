a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# True. a and b have same id due to interning.