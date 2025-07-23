# 19. Check Substring

def is_substring(s1, s2):
    return s2 in s1

print(is_substring("hello world", "world"))  
print(is_substring("hello", "bye"))         
