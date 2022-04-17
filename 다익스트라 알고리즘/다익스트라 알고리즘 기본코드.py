import heapq

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph, start):
    distances = {node:float('inf') for node in graph} # 시작 노드에서 각 노드의 거리의 최솟값을 구하기 위해 무한대로 지정
    distances[start] = 0 # 시작 노드에서 시작노드까지의 거리는 0
    queue = []
    heapq.heappush(queue, [distances[start], start]) # distance, node 순으로 넣어주는 이유는 heap 이 정렬하는 기준이 distance 가 되게 하기 위해
    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        if distances[current_destination] < current_distance: # 현재 노드끼지의 최단거리가 이미 저장되어 있는 경우 (효율성) -> ABDC를 거친 [10,'C'] AEDC를 거친 [8, 'C']가 모두 한 queue 후보로 있을것이고 이미 distance 에는 최단거리인 8이 저장되어 있을테니 쓸모없는 연산을 피하기 위해 미리 최단거리보다 큰 경우 pass 하는 코드 추가
            continue
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return distances

print(dijkstra(graph,'A'))