#  Task : 10. Sum of Digits
# Objective: Find sum of digits in a number.

# By Method 1:-
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))


n=int(input("Enter the number : "))
print(sum_of_digits(n)) 

# By Method 2:-
def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

n=int(input("Enter the number : "))
print(sum_of_digits(n))
