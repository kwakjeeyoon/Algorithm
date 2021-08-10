def solution(N,M,K,li):
    answer = 0
    li.sort(reverse=True)
    count = 0
    for i in range(M):
        if count < K :
            count+=1
            answer += li[0]
        else:
            count = 0
            answer += li[1]
        # print(answer)
    return answer

N, M, K = 5,8,3
li = [2,4,5,4,6]
print(solution(N,M,K,li))