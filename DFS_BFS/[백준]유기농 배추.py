import sys
sys.setrecursionlimit(10**6) # 백준은 재귀가 무한대로 진행될 수 없으니 10의 6승까지 제한을 둬야 recursion error가 안뜬다.

testcase = int(input())

dx,dy = [1,-1,0,0],[0,0,1,-1]

def dfs(x,y):
    graph[x][y] = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
            dfs(nx,ny)

for _ in range(testcase):
    count = 0
    m,n,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int, input().split())
        graph[y][x]=1
    for x in range(n):
        for y in range(m):
            if graph[x][y]:
                dfs(x,y)
                count += 1
    print(count)