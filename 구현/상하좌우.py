def solution(N, li):
    x,y = 0,0
    for i in li:
        if i == 'L':
            new_x, new_y = x - 1, y
        elif i == 'R':
            new_x, new_y = x + 1, y
        elif i == 'U':
            new_x, new_y = x, y - 1
        else:
            new_x, new_y = x, y + 1
        if 0 <= new_x < N and 0 <= new_y < N:
            x, y = new_x, new_y
    return y+1, x+1

N=5
li=['R','R','R','U','D','D']
print(solution(N,li))