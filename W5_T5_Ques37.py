# W5_Task:5- 
# Ques:37. Find K Largest Elements

import heapq

def k_largest(nums, k):
    return heapq.nlargest(k, nums)

print(k_largest([3, 1, 4, 1, 5, 9, 2], 3))

