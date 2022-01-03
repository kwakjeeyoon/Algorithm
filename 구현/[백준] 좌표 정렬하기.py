li = []

x = int(input())
for i in range(x):
    li.append(tuple(map(int, input().split())))

# 1번 방법
li = sorted(li, key = lambda item : (item[0], item[1]))
# 2번 방법
li = sorted(li)

for i in range(x):
    print(li[i][0], li[i][1])

# 완전 뻘짓 했네ㅎㅎㅎ sort 작동 방법을 알아두도록!
# 튜플을 sort하면 지정해주지 않아도 x 기준으로 sort 한 다음 y 기준으로 sort 한다.
# 굳이 지정해주고 싶다면 1번 방법처럼 lambda로 두개를 지정해주면 된다.