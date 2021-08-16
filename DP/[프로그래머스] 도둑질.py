def solution(money):
    dp = [0]*len(money)
    dp[0] = money[0]
    # 첫번째 집은 무조건 터는 경우 -> 마지막 집은 무조건 못턴다
    dp[1] = max(dp[0], money[1]) # 1번 인덱스는 i-2가 없기 때문에 0 과 1중 큰 수를 넣는다
    for i in range(2,len(money)-1): # range에서 마지막 집은 무조건 0으로 비워두기
        dp[i] = max(dp[i-1], dp[i-2]+money[i]) # i-1(이전 집)과 i-2+i(자기자신) 중에 큰것 선택
    dp2 = [0] * len(money)
    dp2[1] = money[1]
    dp2[2] = max(money[1], money[2])
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
    print(dp, dp2)
money = [1,3,5,6,3,2,7,6]
print(solution(money))

