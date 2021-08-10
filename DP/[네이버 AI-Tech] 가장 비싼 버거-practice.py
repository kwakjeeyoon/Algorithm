def solution(N, K, burger, sauce):
    dp = [0]+[10001]*K
    for i in burger:
        for j in range(i, K+1):
            dp[j] = min(dp[j], dp[j-i]+1)
    for i in sauce:
        for j in range(i+1, K+1):
            if dp[j-i] != 10001:
                dp[j] = (dp[j], dp[j-i]+1)
    while True:
        if dp[K] != 10001:
            return K
        else:
            K-=1
N, K = 4, 7000
burger = [3000, 5000]
sauce = [3800, 3000]
print(solution(N, K, burger, sauce))