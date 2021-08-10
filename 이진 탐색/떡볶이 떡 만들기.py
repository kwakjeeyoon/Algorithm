def solution1(N,M,li):
    c = max(li)
    while True:
        count = 0
        for i in li:
            if i-c > 0:
                count += i-c
        if count >= M:
            return c
        c -= 1

def solution(N,M,li):
    answer = 0
    start = 0
    end = max(li)
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for i in li:
            if i-mid > 0:
                total += i-mid
        if total == M:
            answer = mid
            break
        elif total < M:
            end = mid -1
        else:
            answer = mid #### 여기가 진짜 중요요
           start = mid + 1
    return answer

N,M = 4,6
li = [19,15,10,17]
print(solution(N,M,li))