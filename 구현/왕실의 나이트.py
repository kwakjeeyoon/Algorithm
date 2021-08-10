def solution(loc):
    answer = 0
    x = int(ord(loc[0])) - int(ord('a')) + 1
    y = int(loc[1])
    step = [(-1,-2),(-2,-1),(-1,2),(1,-2),(-2,1),(2,-1),(1,2),(2,1)]
    for i in step:
        new_x = x + i[0]
        new_y = y + i[1]
        if 0 < new_x < 8 and 0 < new_y < 8:
            answer += 1
    return answer

loc = 'a1'
print(solution(loc))