def solution(n, times):
    answer = 0
    start = 0
    end = max(times)*n
    while start <= end:
        mid = (start+end)//2
        people = 0
        for i in times:
            people += mid//i
        if people == n:
            return mid
        elif people < n:
            start = mid + 1
        else:
            end = mid - 1
    return answer

times = [7,10]
n=6
print(solution(n,times))