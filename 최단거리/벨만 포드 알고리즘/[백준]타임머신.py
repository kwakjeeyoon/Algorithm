import sys
input = sys.stdin.readline
INF = sys.maxsize
V,E = map(int, input().split())
edges = []
distance = [INF] * (V+1)
for _ in range(E):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))

def bellman_ford(start):
    distance[start] = 0
    for i in range(V):
        for j in range(E):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                if i == V
# 의문점