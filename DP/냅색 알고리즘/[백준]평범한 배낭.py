N,K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(N+1):
    for j in range(K+1):
        weight, value = stuff[i]
        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(value+knapsack[i-1][j-weight], knapsack[i-1][j])
print(knapsack[N][K])

# 문제풀이
# [냅색 알고리즘]
# dp[i][j] = max(dp[i-1][j-value] + value, dp[i-1][j])
# 현재 물건/가치 = (이전 물건의 나의 가치를 뺀 것 + 나의 가치, 이전 물건의 현재 가치) 이 중에 큰 것

# Tip!
# 내 물건을 넣은 뒤 남은 무게를 채울 수 있는 최댓값(dp[i-1][j-weight])을 가져오는 것