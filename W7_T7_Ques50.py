# W7_Task:7- 
# Ques:50. Graph Cycle Detection (Undirected Graph using DFS)
def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False

graph = {0:[1,2], 1:[0,2], 2:[0,1]}
print(has_cycle(graph))  
