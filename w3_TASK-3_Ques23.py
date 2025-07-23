# 23. Find Second Largest

def second_largest(nums):
    if len(nums) < 2:
        return None 

    first = second = float('-inf')
    
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    
    return second if second != float('-inf') else None

print(second_largest([10, 20, 4, 45, 99]))  