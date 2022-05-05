import sys
input = sys.stdin.readline
n,k = map(int, input().split())
li = list(map(int, input().split()))
answer_li = []
sum_li = [0]*(len(li)+1)
for i in range(1, n+1):
    sum_li[i] = li[i-1]+sum_li[i-1]

for j in range(k,n+1):
    answer_li.append(sum_li[j]-sum_li[j-k])

print(max(answer_li))

# 문제풀이
# 누적합에 조건 1개 추가한 문제
# 1) 먼저 주어진 온도의 누적합 리스트(sum_li)를 생성한다.
# 2) range(k,n+1) 개수 만큼 k일 간의 온도를 합한 결과를 answer_li에 저장한다.
# 3) 가장 큰 수를 반환한다. 