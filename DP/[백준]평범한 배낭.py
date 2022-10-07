n,k = map(int, input().split(' '))
li = [tuple(map(int, input().split(' '))) for i in range(n)]
li = sorted(li, key=lambda x:x[0])

dp = [0 for i in range(k+1)]
for w,v in li:
    dp[w] = v
for w,v in li:
    for j in range(w+1, k+1):
        if j-w == w:
            continue
        if j-w > 0:
            dp[j] += dp[j-w]+dp[w]
print(dp[k])

