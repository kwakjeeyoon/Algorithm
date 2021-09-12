import sys
N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

visit = [[0]*M for _ in range(N)]
d = [(-1,0),(1,0),(0,-1),(0,1)]
dd = [[(0, -1), (-1, 0), (0, 1)], [(0, -1), (1, 0), (0, 1)], [(-1, 0), (1, 0), (0, 1)], [(-1, 0), (1, 0), (0, -1)]]

def notdfs(x,y):
    global ans
    for dir in dd:
        temp = arr[x][y]
        for idx in range(3):
            nx = x + dir[idx][0]
            ny = y + dir[idx][1]
            if 0<=nx<N and 0<=ny<M:
                temp+=arr[nx][ny]
            else:
                break
    ans = max(ans, temp)

def dfs(x,y,idx,total):
    global ans
    if idx == 4:
        ans = max(total, ans)
        return
    else:
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0<=nx<N and 0<=ny<M:
                if visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    dfs(nx,ny, idx + 1, total + arr[nx][ny])
                    visit[nx][ny] = 0
for i in range(N):
    for j in range(M):
        dfs(i,j,0,0)
        notdfs(i,j)
print(ans)