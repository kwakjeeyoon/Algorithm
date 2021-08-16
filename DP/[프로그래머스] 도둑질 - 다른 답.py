
def solution(a):
    x1, y1, z1 = a[0], a[1], a[0]+a[2]
    x2, y2, z2 = 0, a[1], a[2]
    for i in a[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1)+i
        x2, y2, z2 = y2, z2, max(x2, y2)+i
        # 여기서 x1,y1에 먼저 y1,z1이 들어가고 max(y1,z1)이 연산되는것 처럼 보이지만
        # 기존의 max(x1,y1)이 연산되어 들어가게 된다.
    return max(x1, y1, y2, z2)

print(solution([1,3,5,6,3,2,7,6]))