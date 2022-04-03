import sys

def logic(n):
    if n==N: # 마지막 행까지 다 돈 경우
        global count
        count += 1 # 경우의 수 1개 추가
    else:
        for i in range(N):
            if visited[i]: # 이미 갔던 열인 경우 뒤의 코드는 실행하지 않음
                continue

            board[n] = i # n 행 i 열에 퀸 놓기
            if check(n): # 상하 좌우 대각선 확인
                visited[i] = True # 열 방문
                logic(n+1) # 다음 행의 퀸 자리
                visited[i] = False # 재귀를 위해 열 방문 해제

def check(n): # 상하 좌우 대각선 확인
    for i in range(n):
        if (board[n]==board[i]) or (n-i == abs(board[n]-board[i])):
            return False
    return True

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    count = 0
    board = [0 for _ in range(N)]
    visited = [False for _ in range(N)]
    logic(0)
    print(count)

# visited 안넣어도 결과는 똑같지만 효율성을 위해 넣어야 한다.