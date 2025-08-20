# W6_Task:6- 
# Ques:44. Maximal Rectangle in Binary Matrix
def maximalRectangle(matrix):
    if not matrix: 
        return 0
    n = len(matrix[0])
    heights = [0] * (n + 1)
    max_area = 0
    for row in matrix:
        for i in range(n):
            heights[i] = heights[i] + 1 if row[i] == 1 else 0
        stack = []
        for i in range(n + 1):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
    return max_area
matrix = [
    [1,0,1,0,0],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,0,1,0]
]
print(maximalRectangle(matrix))  # 6
