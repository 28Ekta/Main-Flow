
# Task 1: Sum of Two Numbers:-
print("Sum of Two Numbers:-")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum_result = a + b
print("Sum:", sum_result)


# Task 2: Odd or Even:-
print(" Odd or Even:-")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Task 3: Factorial Calculation using loop:- 
print("Factorial Calculation using loop")
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial:", factorial)


# Task 4: Fibonacci Sequence:-
print("Fibonacci Sequence")
n = int(input("Enter how many Fibonacci numbers to generate: "))
fib = []
a, b = 0, 1
for _ in range(n):
    fib.append(a)
    a, b = b, a + b
print("Fibonacci Sequence:", fib)


# Task 5: Reverse a String:-
print("Reverse a String")
s = input("Enter a string: ")
reversed_string = s[::-1]
print("Reversed String:", reversed_string)





