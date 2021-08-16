from collections import deque # 양방향에서 처리 할 수 있는 queue 형 자료 구조

'''
###deque 사용법
d.append(x) # 오른쪽에 추가
d.appendleft(x) # 왼쪽에 추가
d.pop() # 오른쪽 삭제 
d.popleft() # 왼쪽 삭제
'''
# n*n 공간의 크기
n = int(input())
# arr 공간의 상태 (9: 아기상어 위치, 0: 빈칸, 그외: 물고기의 위치와 크기)
arr = []

for i in range(n):
    li = list(map(int, input().split()))
    arr.append(li)
    if 9 in li:
        sx,sy = (i, li.index(9)) # x(row),y(col)
        arr[sx][sy] = 0
# print(arr,sx,sy)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

size = 2
move_num = 0
eat = 0
while True:
    q = deque()
    q.append((sx,sy,0))
    visited = [[False]*n for _ in range(n)]
    flag = 1e9
    fish = []
    while q:
        x,y,count = q.popleft()
        if count > flag: # 가장 가까운 거리에 있는 물고기가 아니면 작업 종료
            break
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue # for문에서 continue는 아래 코드 실행하지 않고 넘어가기
            if arr[nx][ny] > size or visited[nx][ny]:
                continue
            if arr[nx][ny] != 0 and arr[nx][ny]<size:
                fish.append((nx,ny,count+1))
                flag=count
            visited[nx][ny] = True
            q.append((nx,ny,count+1))

    if len(fish) > 0:
        fish.sort()
        x,y,move = fish[0][0], fish[0][1], fish[0][2]
        move_num += move
        eat+=1
        arr[x][y] = 0
        if eat == size:
            size+=1
            eat = 0
        sx,sy = x,y
    else:
        break
print(move_num)