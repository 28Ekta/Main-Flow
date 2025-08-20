# W6_Task:6- 
# Ques:42. Merge Intervals

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))  