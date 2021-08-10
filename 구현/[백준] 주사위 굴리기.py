N, M, x, y, n = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
direction = list(map(int, input().split()))

dice = [[0,0,0,0],[0,0,0,0]] # 4,1,3,6 (동+, 서-) /  2,1,5,6 (남 +, 북-)
dx, dy = (0,3)
nx,ny = x,y

for d in direction:
    # 1) 만약 방향이 '동서' dx=0, '남북' dx=1
    if d<=2:
        dx = 0
    else:
        dx = 1