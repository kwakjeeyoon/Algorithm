testcase = int(input())

dx = [-1,-1,1,1,-2,-2,2,2]
dy = [-2,2,-2,2,-1,1,-1,1]

def bfs(graph,n,sx,sy,ex,ey):
    queue = [(sx,sy)]
    while queue:
        x,y = queue.pop(0)
        if (x,y) == (ex,ey):
            return graph[ex][ey]
        for i in range(8):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
                graph[nx][ny]= graph[x][y] + 1
                queue.append((nx,ny))


for _ in range(testcase):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    sx,sy = map(int, input().split())
    ex,ey = map(int, input().split())

    print(bfs(graph,n,sx,sy,ex,ey))