n = int(input())
li = [input().split() for i in range(n)]
for i in range(n):
    li[i].append(i)
li = sorted(li, key = lambda item : (int(item[0]), item[2]))

for i in range(n):
    print(li[i][0], li[i][1])