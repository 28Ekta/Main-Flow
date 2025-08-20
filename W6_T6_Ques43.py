# W6_Task:6- 
# Ques:43. Find the Median of Two Sorted Arrays
def find_median_sorted_arrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    n = len(nums)
    if n % 2 == 1:
        return nums[n//2]
    else:
        return (nums[n//2 - 1] + nums[n//2]) / 2
nums1 = [1, 3]
nums2 = [2]
print(find_median_sorted_arrays(nums1, nums2))

