# V:node // E:edge
V,E = map(int, input().split())
# 시작 노드
start = int(input())
# 단방향 그래프
graph = {(node+1):{} for node in range(V)}
for i in range(E):
    start_node, end_node, weight = map(int, input().split())
    graph[start_node][end_node] = weight
# print(graph)

import heapq

def dijkstra(graph, start):
    # 초기값 'inf'(무한대)로 설정
    distances = {node : float('inf') for node in graph}
    distances[start] = 0 # (시작노드 -> 시작노드) 가중치 == 0
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
dict = dijkstra(graph, 1)
answer = [str(i)+'\n' for i in dict.values()]
# answer = [str(i) for i in dict.values()]
print(''.join(answer), end='\n')