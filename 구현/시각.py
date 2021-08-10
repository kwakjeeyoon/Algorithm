def solution(N):
    answer = 0
    h,m,s = 0,0,0

    while h != N+1:
        s += 1
        if s == 60:
            m += 1
            s = 0
        if m == 60:
            h += 1
            m = 0
        total = str(h) + str(m) + str(s)
        if '3' in total:
            answer += 1

    return answer

N=5
print(solution(N))