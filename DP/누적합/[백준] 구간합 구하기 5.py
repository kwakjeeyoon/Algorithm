import sys
input = sys.stdin.readline
n,m = map(int, input().split())
matrix = []
check = 0
for _ in range(n):
    li = [0]+ list(map(int, input().split()))
    li[0] = check
    for i in range(1, len(li)):
        li[i] = li[i-1]+li[i]
    check = li[-1]
    matrix.append(li)

for _ in range(m):
    sum = 0
    s_x,s_y,e_x,e_y = map(int, input().split())
    for end in range(e_y-s_y-1, e_y):
        sum += matrix[end][e_x]-matrix[end][s_x-1]
        print(matrix[end][e_x],matrix[end][s_x-1])
    print(sum)

# 아직 다 안푼 문제