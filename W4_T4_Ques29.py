# W4_Task:4- 
# Ques:29. Check Pythagorean Triplet

def is_pythagorean_triplet(a, b, c):
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2


print(is_pythagorean_triplet(3, 4, 5)) 