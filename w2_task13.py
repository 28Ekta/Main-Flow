# 13. Sort a List
# Objective: Sort list in ascending order .


def list_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

print(list_sort([5, 1, 4, 2, 8]))   


