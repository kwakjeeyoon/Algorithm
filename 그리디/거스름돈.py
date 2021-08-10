def solution(N):
    money = [500,100,50,10]
    count = 0
    i = 0
    while i < len(money):
        if N >= money[i]:
            count+=1
            N -= money[i]
        else:
            i += 1
    return count
print(solution(1260))