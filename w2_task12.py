# Task :12. List Reversal
# Objective: Reverse a list manually.

# By method 1:-
def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst

print(reverse_list([1, 2, 3, 4]))    

# By method 2:-
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst


print(reverse_list([5, 6, 7, 8]))  
