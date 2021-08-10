def solution(N,M,genre, order):
    answer = []
    genre.sort()
    for target in order:
        start = 0
        end = len(genre)-1
        check = False
        while start <= end:
            mid = (start + end) //2
            if target == genre[mid]:
                check = True
                break
            elif target < genre[mid]:
                end = mid - 1
            else:
                start = mid +1
        answer.append(check)
    return answer

N,M = 5,3
genre = [8,3,7,9,2]
order = [5,7,9]
print(*solution(N,M,genre, order))