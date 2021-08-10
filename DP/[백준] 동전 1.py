def solution(n,k,li):
    dp = [0 for i in range(k+1)]
    dp[0] = 1
    for i in li:
        for j in range(i,k+1):
            if j-i >= 0:
                dp[j] += dp[j-i]
    return dp[k]
n,k = 3,10
li = [1,2,5]
print(solution(n,k,li))