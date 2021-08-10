import itertools

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
# 집과 치킨집의 좌표 계산
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

choice = list(itertools.combinations(chicken, M))
final=[]
for i in choice:
    sum=0
    for j in house:
        distance = []
        x1, y1 = j
        for k in range(len(i)):
            x2,y2 = i[k]
            distance.append(abs(x1-x2)+abs(y1-y2))
        sum+=min(distance)
    final.append(sum)
print(min(final))