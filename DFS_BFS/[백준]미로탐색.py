# BFS 최단거리 문제 1
# 최단경로 탐색 문제에서는 DFS로 하면 모든 경우의 수를 따지고 가장 작은 수를 반환하기 때문에 시간초과가 난다
# 최단경로 문제는 BFS로 풀기!!!!
n,m = map(int, input().split())
graph = []
for _ in range(n):
    row = list(map(int, input()))
    graph.append(row)

def bfs(x,y):
    dx,dy = [1,-1,0,0], [0,0,-1,1]
    count = 0
    queue=[(x,y)]
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1 # 여기가 이 문제의 핵심
    return graph[n-1][m-1]
print(bfs(0,0))

# *** 아이디어 ***
# 한칸식 지나가면서 부모 노드의 개수에 하나씩 더하여 앞으로 나아가는 문제
# 전형적인 문제이기 때문에 위의 아이디어 암기하기!