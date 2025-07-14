# 14. Remove Duplicates
# Objective: Remove duplicates from a list.

# Method 1 – Using a set (preserves no order):


def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 7, 9, 4, 3, 1]))   

# Method 2 – Preserve order:

def remove_duplicates_ordered(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates_ordered([1, 2, 2, 5, 6, 1, 5, 3, 1]))




