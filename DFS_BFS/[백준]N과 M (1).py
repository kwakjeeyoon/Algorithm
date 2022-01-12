n, m = map(int, input().split())

s = []

def dfs():
    if len(s) == m:
        return print(' '.join(map(str, s)))

    for i in range(1,n+1):
        if i not in s :
            if s:
                if s[-1]<i:
                    s.append(i)
            else:
                s.append(i)
            dfs()
            s.pop()

dfs()