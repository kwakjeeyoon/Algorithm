import sys
input = sys.stdin.readline
time = {}
n = int(input())
for _ in range(n):
    start, end = map(int, input().split())
    time[(start,end)] = end-start

time = [k for k,v in sorted(time.items(), key=lambda x: x[1])]
answer = 0
check = [0]*(2**31-1)
for start,end in time:
    flag = True
    for i in range(start, end):
        if check[i]:
            flag = False
            break
    if flag:
        for i in range(start, end):
            check[i] = 1
        answer += 1
print(answer)