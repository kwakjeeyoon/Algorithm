def solution(n, target, li):
    answer = 0
    li.sort()
    start = 0
    end = len(li) -1
    while start <= end:
        now =(end + start) // 2
        if target == li[now]:
            return now
        elif target < li[now]:
            end = now-1
        else:
            start = now+1
    return None

n, target = 10, 7
li = [1,3,5,9,11,13,15,17,19]
print(solution(n,target,li))