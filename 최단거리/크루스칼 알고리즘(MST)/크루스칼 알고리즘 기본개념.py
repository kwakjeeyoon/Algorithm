graph = [(1,2,13),(1,3,5),(2,4,9),(3,4,15),(3,5,3),(4,5,1),(4,6,7),(5,6,2)]
# 1) 먼저 cost 기준으로 오름차순 정렬
graph.sort(key = lambda x:x[2])

n = 6 # 노드의 개수
p = [0] # 각 노드의 root를 담을 리스트

# 2) 먼저 자기 자신을 root로 저장
for i in range(1,n+1):
    p.append(i)

def find(u):
    if u!=p[u]:
        p[u]=find(p[u])
    return p[u]

def union(u,v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1

mst = []
tree_edges = 0 # 현재 지나간 엣지의 개수
mst_cost = 0

while True:
    if tree_edges == n-1:
        break
    u,v,wt = graph.pop(0)
    if find(u)!=find(v):
        union(u,v)
        mst.append((u,v))
        tree_edges += 1
        mst_cost += wt

print(mst_cost)

