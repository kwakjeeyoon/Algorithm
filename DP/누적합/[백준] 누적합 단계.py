# prefix sum : 누적 합
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

num = list(map(int, input().split()))
li = [0 for _ in range(n+1)]

for i, now in enumerate(num):
    li[i+1] = li[i]+num[i]

for _ in range(m):
    start, end = map(int, input().split())
    answer = li[end] - li[start-1]
    print(answer)

# 문제풀이
# 처음 풀이 방법은 맨 처음 수는 li에 먼저 넣어놓고 그 다음에 들어오는 수를 앞에 수랑 더하는 방식으로 했다.
# 이 방법의 문제는 0부분을 비워놓지 않으면 1~3이라는 구간이 주어질 때 li[start-1]부분이 리스트의 맨 마지막
# 부분을 뜻하게 된다.
# DP 문제는 처음 0 부분을 비워놓고 시작하는게 좋다.

