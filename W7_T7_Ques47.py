# W7_Task:7- 
# Ques:47. Count Inversions (Modified Merge Sort)
def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = merge_sort_count(arr[:mid])
    right, inv_right = merge_sort_count(arr[mid:])
    merged, inv_split = merge_and_count(left, right)
    return merged, inv_left + inv_right + inv_split
def merge_and_count(left, right):
    i = j = inv_count = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv_count
arr = [2, 4, 1, 3, 5]
_, inversions = merge_sort_count(arr)
print("Inversions:", inversions)  




