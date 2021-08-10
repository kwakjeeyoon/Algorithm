def solution(N,M,arr):
    arr = [list(map(int, i)) for i in arr]
    visited = [(0,0)]
    queue = [(0,0)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y = queue.pop()
        for i in direction:
            new_x, new_y = x + i[0], y + i[1]
            if 0 <= new_x < N and 0 <= new_y < M and arr[new_y][new_x] != 0 and ((new_x, new_y) not in visited):
                arr[new_y][new_x] += arr[y][x]
                queue.append((new_x, new_y))
                visited.append((new_x, new_y))
    return arr[N-1][M-1]
N,M = 3,3
arr = ['110','010','011']
print(solution(N,M,arr))