import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
li.sort()

def split_find(target):
    start,end = 0, len(li)-1
    while start <= end:
        now = (start+end)//2
        if li[now] == target:
            return 1
        elif li[now] > target:
            end = now - 1
        else:
            start = now + 1
    return 0

for target in targets:
    print(split_find(target))

# 문제풀이
# 가장 기본적인 이분탐색 문제