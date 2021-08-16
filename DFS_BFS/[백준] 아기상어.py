from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    li = list(map(int, input().split()))
    if 9 in li:
        sx,sy = i, li.index(9)
        li[sy] = 0
    arr.append(li)

# print(arr, sx,sy)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

size = 2
move_num = 0
eat = 0
while True:
    q = deque()
    flag = 1e9
    q.append((sx,sy,0))
    visited = [[False]*n for _ in range(n)]
    fish = []
    while q:
        x,y,count = q.popleft()
        if flag < count: break
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if arr[nx][ny]>size or visited[nx][ny]:
                continue
            if arr[nx][ny]!=0 and arr[nx][ny] < size:
                fish.append((nx,ny,count+1))
                flag = count
            q.append((nx,ny,count+1))
            visited[nx][ny] = True
    if fish:
        fish.sort()
        x,y,move = fish[0]
        arr[x][y] = 0
        move_num += move
        eat += 1
        if eat == size:
            size+=1
            eat = 0
        sx,sy = x,y
    else: break
print(move_num)