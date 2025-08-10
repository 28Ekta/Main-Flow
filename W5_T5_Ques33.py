# W5_Task:5- 
# Ques:33. Find All Permutations of a String

from itertools import permutations

def string_permutations(s):
    return [''.join(p) for p in permutations(s)]


print(string_permutations("abc"))

