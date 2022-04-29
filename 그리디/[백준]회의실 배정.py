import sys
input = sys.stdin.readline
time = []
n = int(input())
for _ in range(n):
    time.append(list(map(int, input().split())))

test = [i for i in sorted(time, key=lambda x: (x[1],x[0]))]

answer = 0
now_s = 0
now_e = 0
for start, end in test:
    if now_e <= start:
        answer += 1
        now_s = start
        now_e = end
print(answer)

# 문제풀이
# 정렬 기준으로 두 가지로 해야한다.
# 1. (start,end) 에서 end 를 기준으로 회의 시간을 정렬
# 2. (start,end) 에서 start를 기준으로 다시 정렬 한다
# -> 2번의 예외상황 : (2,2)(1,2)일 경우 (1,2) 를 먼저 하면 (1,2)(2,2) 모두 포함시킬 수 있기 때문
# 시작과 동시에 끝나는 경우가 있는것을 고려