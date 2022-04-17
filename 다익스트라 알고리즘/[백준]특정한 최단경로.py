import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
N,E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
v1,v2 = map(int, input().split())

def dijkstra(start, end):
    distances = {node:INF for node in range(1,N+1)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))
    while queue:
        now_w, now_n = heapq.heappop(queue)
        if distances[now_n] < now_w:
            continue
        for new_w, new_n in graph[now_n]:
            dist = now_w + new_w
            if dist < distances[new_n]:
                distances[new_n] = dist
                heapq.heappush(queue, (distances[new_n], new_n))
    return distances[end]

def solution():
    check = []
    cand_list = [[1, v1, v2, N], [1, v2, v1, N]]
    for cand in cand_list:
        answer = 0
        for i in range(len(cand)-1):
            start = cand[i]
            end = cand[i+1]
            dist = dijkstra(start, end)
            if dist == INF:
                return -1
            answer += dist
        check.append(answer)
    # print(check)
    return min(check)

print(solution())

# 오답노트
# 처음에는 1 -> v1 -> v2 -> N 로 가는 경로만 있다고 생각했는데 v1, v2를 반드시 지나가려면
# [1-v1-v2-N], [1,v2,v1,N] 이렇게 두가지 경로가 있다

# 코딩을 하기 전에 문제정의에 시간을 더 투자하자. 당연히 할 수 있는 생각을 놓치고 넘어간다.