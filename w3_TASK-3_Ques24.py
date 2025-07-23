# 24. Check Anagram

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(is_anagram("listen", "silent"))  
print(is_anagram("hello", "world"))   
