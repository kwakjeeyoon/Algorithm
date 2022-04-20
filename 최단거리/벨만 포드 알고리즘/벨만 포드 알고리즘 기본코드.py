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
                if i == V-1:
                    return True
    return False

negative_cycle = bellman_ford(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, V+1):
        print("-1" if distance[i] == INF else distance[i])


# 의문점
# for문을 돌려서 반복하여 모든 엣지가 노드의 최단거리를 갱신하는지 여부를 판별하는 것까지 알겠다
# 하지만 왜 노드의 개수만큼 for문을 반복하는지는 모르겠다. 왜 딱 노드의 마지막 for문에서 갱신여부를 판별하는지 이해가 되지 않는다.

1num =