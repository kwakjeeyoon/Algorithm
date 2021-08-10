def solution(N,M,map):
    for i in range(N):
        for j in range(M):
            if i ==0 and j!=0:
                map[i][j] += map[i][j-1]
            elif i!=0 and j == 0:
                map[i][j] += map[i-1][j]
            elif i!=0 and j!=0:
                map[i][j] += max(map[i-1][j-1], map[i-1][j], map[i][j-1])
    return map[N-1][M-1]
N,M = 3,4
map = [[1,2,3,4],[0,0,0,5],[6,7,8,9]]
print(solution(N,M,map))