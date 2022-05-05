import sys
input = sys.stdin.readline
s = list(input())
q = int(input())

alpha = set(s)
sum = {k:[0]*(len(s)+1) for k in alpha}
for a in alpha:
    for i, b in enumerate(s):
        if a==b:
            sum[a][i+1] = sum[a][i]+1
        else:
            sum[a][i+1] = sum[a][i]

for _ in range(q):
    alphabet, start, end = input().split()
    try:
        l = sum[alphabet]
        print(l[int(end)+1]-l[int(start)])
    except:
        print(0)
