from collections import defaultdict
node = int(input())
link = int(input())
graph = defaultdict(list)
for _ in range(link):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, visited):
    queue = [start]
    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n]
    return visited
print(len(bfs(1, []))-1)

def dfs(start, visited):
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            dfs(i, visited)
    return visited
print(len(dfs(1, []))-1)