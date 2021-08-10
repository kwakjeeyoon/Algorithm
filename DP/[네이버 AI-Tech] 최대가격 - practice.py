def solution(N, M, map):
    for x in range(N):
        for y in range(M):
            if x==0 and y!=0:
                map[x][y] += map[x][y-1]
            elif x!=0 and y==0:
                map[x][y] += map[x-1][y]
            elif x!=0 and y!=0:
                map[x][y] += max(map[x-1][y], map[x][y-1], map[x-1][y-1])
    return map[N-1][M-1]

N, M = 3, 4
map = [[1, 2, 3, 4], [0, 0, 0, 5], [6, 7, 8, 9]]
print(solution(N, M, map))