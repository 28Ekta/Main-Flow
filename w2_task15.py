# 15. String Length (Without len())
# Objective: Find length of a string manually.

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

string =input("Enter Your String : ")
print(string_length(string))   
