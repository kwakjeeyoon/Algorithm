def dfs(start, arr):
    y,x = start
    direction=[(-1,0),(1,0),(0,-1),(0,1)]
    if arr[y][x] == '0':
        arr[y][x] = '1'
        for i in direction:
            new_y, new_x = x+i[0], y+i[1]
            if 0 <= new_x < len(arr[0]) and 0<= new_y < len(arr):
                # print(new_x, new_y)
                dfs((new_y, new_x), arr)
    return arr

def solution(arr):
    answer = 0
    arr = [list(i) for i in arr]
    N,M = len(arr), len(arr[0])
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '0':
                arr = dfs((i,j), arr)
                answer += 1
    return answer
arr = ['00110','00011','11111','00000']
print(solution(arr))