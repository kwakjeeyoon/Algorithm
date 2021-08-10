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
def dijkstra(graph, start):
    distances = {node:max for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        if distances[current_destination] < current_distance:
            continue
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return distances

dict = dijkstra(graph,1)
for i in dict.values():
    if i!=max:
        print(i)
    else:
        print('INF')