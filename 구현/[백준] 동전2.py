n,k = map(int, input().split())
coins = [int(input()) for i in range(n)]
li = [0]+[float('inf') for i in range(k)]
for coin in coins:
    for i in range(coin,k+1):
        li[i] = min(li[i], li[i-coin]+1)
if str(li[-1])!='inf':
    print(li[-1])
else:
    print(-1)