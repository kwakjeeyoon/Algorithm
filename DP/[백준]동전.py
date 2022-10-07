test_n = int(input())
for i in range(test_n):
    answer = 0
    num = input()
    coins = list(map(int, input().split(' ')))
    money = int(input())
    dp = [0 for i in range(money+1)]
    dp[0]=1
    for c in coins:
        for j in range(c, money+1):
            if j-c >= 0:
                dp[j]+=dp[j-c]
    print(dp[money])