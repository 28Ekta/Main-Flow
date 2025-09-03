# W8_Task:8- 
# Ques:60. Find All Paths in a Graph (DFS + Backtracking)

def all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = all_paths(graph, node, end, path)
            for p in new_paths:
                paths.append(p)
    return paths