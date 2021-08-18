def hanoi(n,start,end,mid, result):
    if n==1:
        return result.append([start,end])
    hanoi(n-1,start,mid,end)
    result.append([start,end])
    hanoi(n-1,mid,end,start)
    return result


def solution(n):
    result = []
    hanoi(n, 1, 3, 2, result)
    return result

print(solution(3))