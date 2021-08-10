import sys
input = sys.stdin.readline
V,E = map(int, input().split())
start = int(input())
graph = {(node+1):{} for node in range(V)}
for i in range(E):
    start_node, end_node, weight = map(int, input().split())
    graph[start_node][end_node] = weight
# print(graph)

max = sys.maxsize

import heapq
import collections
def dijkstra(graph, start):
    queue = [(0,start)]
    distances = collections.defaultdict(int)
    while queue:
        dist, node = heapq.heappop(queue)
        if node not in distances:
            distances[node] = dist
            for new_destination, new_distance in graph[node].items():
                distance = dist + new_distance
                if distance < distances[new_destination]:
                    distances[new_destination] = distance
                    heapq.heappush(queue, (distance, new_destination))
    return distances

dict = dijkstra(graph,1)
for i in dict.values():
    if i!=max:
        print(i)
    else:
        print('INF')