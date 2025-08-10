# W5_Task:5- 
# Ques:36. Longest Increasing Subsequence (LIS)

def length_of_LIS(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]))