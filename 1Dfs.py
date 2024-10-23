def dfs(graph,node,path = []):
    path.append(node)

    for i in graph[node]:
        if i not in path:
            dfs(graph,i,path)

    return path

graph = {
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F','G'],
    'D':['B'],
    'E':['B','H'],
    'F':['C'],
    'G':['C'],
    'H':['E']
}

print(dfs(graph,'A'))