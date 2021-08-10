import sys
input = sys.stdin.readline

N = int(input()) # 보드의 크기
K = int(input()) # 사과의 개수

apple = [tuple(map(int, input().split())) for i in range(K)] # 사과의 위치
d_num = int(input()) # 방향 전환의 수
snake_dir = [tuple(input().split()) for i in range(d_num)] # 방향 전환 타이밍 (time, direction)

direction = [(0,1),(1,0),(0,-1),(-1,0)]
idx = 0 # 현재 방향
now = (1,1) # 현재 위치
times = 0
snake = [(1,1)] # 뱀의 몸이 있는 위치

while True:
    times += 1
    now = (now[0]+direction[idx][0], now[1]+direction[idx][1])
    if 0< now[0] <=N and 0< now[1] <= N: # 벽에 부딪히지 않는 경우
        if now in snake: # 몸에 부딪히는 경우
            break
        if now in apple: # 현재 위치에 사과가 있는 경우
            #1) 사과 없애기
            i = apple.index(now)
            apple.pop(i)
            #2) 꼬리가 움직이지 않게
            snake.append(now)
        else:
            snake.pop(0)
            snake.append(now)
        # 방향 전환
        if snake_dir and times == int(snake_dir[0][0]):
            t,d = snake_dir.pop(0)
            if d == 'D':
                idx += 1
            else:
                idx -= 1
            idx = idx%4
    else: # 벽에 부딪히는 경우
        break

print(times)