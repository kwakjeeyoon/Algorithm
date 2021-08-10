N,L,R = map(int, input().split())
arr = []
total_visited=[]
answer = 0

for i in range(N):
    cell = list(map(int, input().split()))
    arr.append(cell)

def bfs(x,y):
    visited = [(x,y)]
    queue = [(x,y)]
    sum = 0
    count = 0

    operation_x = [0,0,-1,1]
    operation_y = [-1,1,0,0]

    while queue:
        x,y = queue.pop()
        sum += arr[x][y]
        count += 1

        for i in range(4):
            new_x, new_y = x + operation_x[i], y + operation_y[i]
            if 0<= new_x < N and 0<= new_y < N and (new_x,new_y) not in visited and (new_x, new_y) not in visited:
                sub = arr[x][y] - arr[new_x][new_y]
                if L<= abs(sub) <= R:
                    global is_move
                    is_move = True

                    queue.append((new_x, new_y))
                    visited.append((new_x, new_y))
    return visited, sum//count


while True:
    for i in range(N):
        for j in range(N):
            if (i,j) not in total_visited:
                visited, change = bfs(i,j)
                visited.append((i,j))
                total_visited.append(visited)
    for x,y in visited:
        arr[x][y] = change

    if not is_move:
        break
    answer += 1

print(answer)