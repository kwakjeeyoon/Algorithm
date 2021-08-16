'''
# 풀이 과정
1. 먼저 초기에 상어가 있는 위치를 sx,sy에 담고 0으로 바꿔준다
2. bfs로 내 위치 주변의 모든 곳을 탐색해서 먹을 수 있는 물고리의 위치를 fish에 넣는다.
여기서 만약 상어와 물고기의 거리가 더 먼 위치의 물고기라면 탐색을 중단한다.
(어쩌피 그 거리에서  + 1 하면 더 멀어질 것이기 때문)
3. 갈 수 있는 모든 fish를 담았으면 (x,y,count)로 sort 한다.
(count는 제일 작은 것만 담기기 때문에 상관하지 않는다.)
4. 제일 가까운 위치의 fish를 뽑고 그 위치를 다시 상어의 위치로 갱신해준다.
이 과정에서 움직이는데 걸린 시간을 move_num에 더하고
상어의 크기가 커지는 시점을 고려해 주기 위해 먹은 물고기 수를 +1 을 해주거나
몸사이즈와 같은 수의 물고기를 먹으면 상어의 size + 1을 해주고 eat = 0으로 갱신한다.
'''

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