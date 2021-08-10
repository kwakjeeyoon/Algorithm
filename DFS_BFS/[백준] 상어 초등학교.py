# BFS 문제로 접근
N = int(input())
arr = [[0]*N for i in range(N)]
like = []
for i in range(N**2):
    li = list(map(int, input().split()))
    like.append(li)
dic = {}

x_operate=[0,0,-1,1]
y_operate=[-1,1,0,0]

def like_count(num, li):
    first = {}
    second = {}
    for i in range(N**2):
        first[i] = 0
        second[i] = 0
        x = i//N
        y = i%N
        if arr[x][y] == 0:
            for d in range(4):
                new_x = x + x_operate[d]
                new_y = y + y_operate[d]
                if 0<=new_x<N and 0<=new_y<N:
                    if arr[new_x][new_y]==0:
                        second[i] += 1
                    elif arr[new_x][new_y] in li:
                        first[i] += 1
    compare = sorted(first.items(), key=lambda x: x[1], reverse=True)
    if compare[0][1] != compare[1][1]:
        loc = compare[0][0]
    else:
        candidate = {}
        for k in compare:
            if k[1] == compare[0][1]:
                candidate[k[0]]=second[k[0]]
            else:
                break
        compare = sorted(candidate.items(), key=lambda x: x[1], reverse=True)
        loc = compare[0][0]
    x = loc // N
    y = loc % N
    arr[x][y] = num
for i in like:
    like_count(i[0], i[1:])
    dic[i[0]] = i[1:]
answer = 0
for i in range(N**2):
    count = 0
    x = i//N
    y = i%N
    original = arr[x][y]
    for d in range(4):
        new_x = x + x_operate[d]
        new_y = y + y_operate[d]
        if 0 <= new_x < N and 0 <= new_y < N:
            num = arr[new_x][new_y]
            if num in dic[original]:
                count+=1
    if count == 1:
        answer += 1
    elif count == 2:
        answer += 10
    elif count == 3:
        answer += 100
    elif count == 4:
        answer += 1000
print(answer)