N,L,R = map(int, input().split())
arr = []
total_visited = []
visited=[]
answer = 0

for i in range(N):
    cell = list(map(int, input().split()))
    arr.append(cell)

def bfs(x,y, arr):
    visited = [(x,y)]
    queue = [(x,y)]
    num = 0
    count = 0
    operate_x = [0, 0, -1, 1]
    operate_y = [-1, 1, 0, 0]
    while queue:
        x,y = queue.pop()
        for i in range(4):
            new_x, new_y = x + operate_x[i], y+operate_y[i]
            if 0 <= new_x < N and 0 <= new_y < N and ((new_x, new_y) not in visited)  :
                sub = arr[x][y] - arr[new_x][new_y]
                if L <= abs(sub) <= R:
                    total_visited.append((new_x,new_y))
                    visited.append((new_x,new_y))
                    queue.append((new_x, new_y))
                    num+=arr[new_x][new_y]
                    count+=1
    return visited, num//count

check = False
while not check:
    for i in range(N):
        for j in range(N):
            if (i,j) not in total_visited:
                visited, change = bfs(i,j, arr)
                if len(num)>1:
                    for x,y in visited:
                        arr[x][y]=change
                    answer += 1
                    check = True
                    print(visited, num, answer, change)
                    print(arr)
                else:
                    False