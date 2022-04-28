import sys
input = sys.stdin.readline
n,k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

answer = 0
coins = sorted(coins, reverse=True)
for coin in coins:
    if coin <= k:
        num = k//coin
        answer += num
        k -= num*coin
print(answer)

# ***문제풀이***
# 이 문제에서 그리디가 만족하는 이유는 " A1 = 1" 라는 조건이 있었기 때문이다.
# 1 이라는 화폐가 있는 한 가장 큰 화폐부터 금액을 채워서 나머지는 1로 처리할 수 있기 때문