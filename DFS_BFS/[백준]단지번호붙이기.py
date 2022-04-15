n = int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input())))

count = 0
output = []
dx,dy = [1,-1,0,0], [0,0,1,-1]

def dfs(x,y):
    global count
    if 0 <= x < n and 0 <= y < n and graph[x][y]==1:
        graph[x][y] = 0
        count += 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            dfs(nx,ny)

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            dfs(x,y)
            output.append(count)
            count=0
print(len(output))
output.sort()
for i in output:
    print(i)
