def solution(n):
    arr = [[0 for j in range(i)] for i in range(n,0,-1)]
    x, y = -1, n
    idx = 0
    for i in range(n):
        for j in range(i,n):
            idx+=1
            if i%3 == 0:
                x+=1
                y-=1
            elif i%3 == 1:
                x-=1
            else:
                y+=1
            arr[x][y]=idx
    return arr

n = 5
print(solution(n))