# 18. Swap Two Numbers (Without Third Variable)

def swap_numbers(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    a = a + b
    b = a - b
    a = a - b
    print(f"After swapping: a = {a}, b = {b}")

swap_numbers(10, 20)
