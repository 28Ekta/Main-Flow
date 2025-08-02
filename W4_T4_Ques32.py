# W4_Task:4- 
# Ques:32. Find Subarray with Given Sum

def subarray_sum(arr, target):
    curr_sum = 0
    start = 0
    for end in range(len(arr)):
        curr_sum += arr[end]
        while curr_sum > target and start < end:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == target:
            return (start, end)
    return -1


print(subarray_sum([1, 4, 20, 3, 10, 5], 33))