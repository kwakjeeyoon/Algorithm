graph = {'A':['B','C'],
         'B':['A','D','E'],
         'C':['A','G','H'],
         'D':['B'],
         'E':['B','F'],
         'F':['E'],
         'G':['C'],
         'H':['C']}

def bfs(graph, root):
    visited =[]
    queue = [root]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n]
    return visited
print(bfs(graph, 'A'))

def dfs(graph, root, visited = []):
    visited.append(root)

    for n in graph[root]:
        if n not in visited:
            dfs(graph, n, visited)
    return visited
print(dfs(graph,'A'))
