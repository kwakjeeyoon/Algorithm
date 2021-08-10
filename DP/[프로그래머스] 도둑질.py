def solution(money):
    dp = [0]*len(money)
    dp[0] = money[0]
    dp[1] = max(dp[0], money[1])
    for i in range(2,len(money)-1):
        dp[i] = max(dp[i-1], dp[i-2]+money[i])
    dp2 = [0] * len(money)
    dp2[1] = money[1]
    dp2[2] = max(money[1], money[2])
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
    print(dp, dp2)
money = [1,3,5,6,3,2,7,6]
print(solution(money))

