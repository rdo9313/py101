def triangle(n):
    for num in range(1, n + 1):
        print(" " * (n - num) + "*" * num)

triangle(5)
triangle(9)
