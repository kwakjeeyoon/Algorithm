n,k = map(int, input().split(' '))
dp = [0 for i in range(k+1)]
dp[0] = 1
coins = [int(input()) for i in range(n)]
coins.sort()
for i in coins:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
print(dp[k])