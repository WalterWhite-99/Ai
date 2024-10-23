def bfs(graph,node,path=[],index=0):
    path.append(node)

    while index != len(path):
        for i in graph[path[index]]:
            if i not in path:
                path.append(i)
        index +=1
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

print(bfs(graph,'A'))