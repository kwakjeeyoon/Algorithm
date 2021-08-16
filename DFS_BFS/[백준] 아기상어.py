N = int(input())
arr = []
for i in range(N):
    li = list(map(int, input().split()))
    arr.append(li)
    if 9 in li:
        loc = (i, li.index(9)) # x(row),y(col)

dir_x = [0,0,-1,1]
dir_y = [-1,1,0,0]

score = 2
visited = [loc]
queue = [loc]
li=[]
while queue:
    while True:
        # time += 1
        loc = queue.pop(0)
        for i in range(4):
            nx,ny = loc[0]+dir_x[i], loc[1]+dir_y[i]
            if 0<= nx < N and 0<= ny < N and (nx,ny) not in visited and arr[nx][ny] <=2:
                if arr[nx][ny] == 1:
                    li.append((nx,ny))
                queue.append((nx,ny))
                visited.append((nx,ny))
        if li:
            li.sort()
            loc = li[0]
            break

