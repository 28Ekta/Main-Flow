# W5_Task:5- 
# Ques:35. Find Duplicates in a List

from collections import Counter

def find_duplicates(lst):
    counts = Counter(lst)
    return [item for item, count in counts.items() if count > 1]


print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))