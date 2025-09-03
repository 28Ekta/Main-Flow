# W7_Task:7- 
# Ques:49. Traveling Salesman Problem (TSP - DP with Bitmasking)
def tsp(dist):
    n = len(dist)
    VISITED_ALL = (1 << n) - 1

    from functools import lru_cache
    @lru_cache(None)
    def dp(mask, pos):
        if mask == VISITED_ALL:
            return dist[pos][0] 
        ans = float('inf')
        for city in range(n):
            if mask & (1 << city) == 0:
                ans = min(ans, dist[pos][city] + dp(mask | (1 << city), city))
        return ans
    return dp(1, 0)
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print("TSP Min Distance:", tsp(dist))  # Output: 80
