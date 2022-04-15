n,k = map(int, input().split())
loc = [0]*100001

# 맞은 코드
def bfs():
    queue = [n]
    while queue:
        x = queue.pop(0)
        if x==k:
            return loc[k]
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=100000 and loc[nx]==0:
                queue.append(nx)
                loc[nx] = loc[x] + 1

print(bfs())

# 틀린 코드
def bfs_false():
    queue = [n]
    while queue:
        if loc[k] != 0:
            return loc[k]
        x = queue.pop(0)
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=100000 and loc[nx]==0:
                queue.append(nx)
                loc[nx] = loc[x] + 1

print(bfs_false())

# testcase : 100000 100000 -> 맞은 : 0 / 틀린 : 2
# 코드가 틀린 이유는 실제 답이 0인 경우 답을 할 수 없기 때문이다.
# x-1 x+1 x*2는 무조건 다 다른 수가 되기 때문에 queue에 넣고 해당 수가 나올때 값을 reutrn 하더라도 틀린 코드가 되지 않는다.