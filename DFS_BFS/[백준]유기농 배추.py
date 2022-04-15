testcase = int(input())

dx,dy = [1,-1,0,0],[0,0,1,-1]
def dfs(x,y, M,N):
    if 0<=x<N and 0<=y<M and graph[y][x] == 1:
        graph[y][x] = 0
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            dfs(nx,ny,M,N)

graph = []
count = 0
for _ in range(testcase):
    M,N,K = map(int, input().split())
    for _ in range(N):
        graph.append([0]*M)
    for _ in range(K):
        x,y = map(int, input().split())
        graph[y][x] = 1
    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                dfs(x,y,M,N)
                count += 1
    print(count)
    graph = []
    count = 0
