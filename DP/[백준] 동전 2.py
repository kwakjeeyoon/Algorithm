def solution(N,K,li):
    dp = [10001] * (K+1)
    dp[0] = 0
    for i in li:
        for j in range(i,K+1):
            dp[j] = min(dp[j], dp[j-i]+1)

    dp[-1] = dp[-1] if dp[-1] != 10001 else -1
    return dp[-1]

N,K = 3,15
li = [1,5,12]
print(solution(N,K,li))