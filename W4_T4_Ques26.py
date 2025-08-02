# W4_Task:4- 
# Ques:26. Check Balanced Parentheses

def is_balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack


print(is_balanced("{[()]}")) 
print(is_balanced("{[(])}")) 