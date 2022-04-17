import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize

V,E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u-1].append((w,v))

def dijkstra(start):
    distances = {node:INF for node in range(1,V+1)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue
        for new_distance, new_node in graph[current_node-1]:
            distance = new_distance + current_distance
            if distance < distances[new_node]:
                distances[new_node] = distance
                heapq.heappush(queue, (distance, new_node))
    return distances

distances = dijkstra(start)

for node in range(1, V+1):
    print('INF' if distances[node] == INF else distances[node])

# 오답노트
# 조건 : 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
# 위의 조건이 붙으면 graph가 dict 타입인 경우 반례가 존재할 수 있다. 하나의 노드에 여러 값을 저장할 수 없기 때문이다.