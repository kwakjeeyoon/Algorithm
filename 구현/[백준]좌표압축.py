n = int(input())
li = list(map(int, input().split()))
sub_li = sorted(list(set(li)))
answer = {}
for i in range(len(sub_li)):
    answer[sub_li[i]] = i
final = []
for i in range(n):
    final.append(answer[li[i]])
print(*final)