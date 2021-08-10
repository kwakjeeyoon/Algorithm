def find(u, p):
    if u != p[u]:
        p[u] = find(p[u],p)
    return p[u]
def union(u,v,p):
    root1 = find(u,p)
    root2 = find(v,p)
    p[root1] = root2
    return p
def solution(N, cost):
    p = [i for i in range(N)]
    cost.sort(key = lambda x:x[2])
    tree_edges = 0
    c = 0
    mst = []
    while tree_edges != N-1:
        u,v,wt = cost.pop(0)
        if find(u,p) != find(v,p) :
            p = union(u,v,p)
            mst.append((u,v))
            tree_edges += 1
            c += wt
    return c

N = 4
cost = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(N, cost))