# Task : 11. LCM and GCD
# Objective: Find LCM and GCD of two integers.

import math

def gcd_lcm(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a * b) // gcd if gcd != 0 else 0
    return f"the gcd is {gcd}", f"the lcm is {lcm}"

n=int(input("Enter the value of a : "))
m=int(input("Enter the value of b : "))
print(gcd_lcm(n, m))  
