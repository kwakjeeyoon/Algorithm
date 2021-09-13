from collections import defaultdict
N,M,V = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, visited):
    queue = [start]
    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            graph[n].sort()
            queue += graph[n]
    return visited
def dfs(start, visited):
    stack = [start]
    visited.append(start)
    graph[start].sort()
    for node in graph[start]:
        if node not in visited:
            dfs(node, visited)
    return visited

print(*dfs(V, []))
print(*bfs(V, []))

