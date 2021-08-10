def solution(N,K):
    answer = 0
    while N != 1:
        if N % K == 0:
            N = N//K
        else:
            N-=1
        answer+=1
    return answer

N, K = 25,5
print(solution(N,K))