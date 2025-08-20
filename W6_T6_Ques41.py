# W6_Task:6- 
# Ques: 41. Knapsack Problem (0/1)

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

weights = [1, 2, 3]
values = [60, 100, 120]
capacity = 5
print(knapsack(weights, values, capacity)) 
