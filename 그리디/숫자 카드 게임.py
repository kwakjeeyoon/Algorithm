def solution(N,M,arr):
    li = []
    for i in arr:
        li.append(min(i))
    return max(li)

N, M = 3,3
arr = [[3,1,2],[4,1,4],[2,2,2]]
print(solution(N,M,arr))