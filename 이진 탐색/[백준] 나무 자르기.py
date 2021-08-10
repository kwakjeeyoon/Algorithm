N,M = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)

while start <= end:
    mid = (start+end)//2
    sum = 0
    # mid가 나무길이 일때, 얻을 수 있는 나무의 길이
    for i in trees :
        if i > mid:
            sum += i-mid
    if sum == M:
        answer = mid
        break
    elif sum > M:
        answer = mid
        start = mid +1
    elif sum < M :
        end = mid-1
print(answer)

# while start <= end:
#     mid = (start+end)//2
#     sum = 0
#     for i in trees :
#         if i > mid:
#             sum += i-mid
#     if sum >= M:
#         start = mid +1
#     elif sum < M :
#         end = mid-1
# print(end, start)

