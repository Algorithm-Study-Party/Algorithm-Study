import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c)) # 방향성 없는 그래프니까 x,y와 y,x 모두 추가

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF]*(N+1) # dijkstra를 나눠서 여러번 구하기 때문에 distance 매번 초기화 되야 하고
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        w, v = heapq.heappop(q)
        if distance[v] < w:
            continue
        for vertex, weight in graph[v]:
            cost = w + weight
            if cost < distance[vertex]:
                distance[vertex] = cost
                heapq.heappush(q, (cost, vertex))
    return distance
# 1 -> v1 -> v2 -> N의 경우와 1 -> v2 -> v1 -> N의 경우를 나눠서 생각
path1 = dijkstra(1)
path2 = dijkstra(v1)
path3 = dijkstra(v2)
dist1 = path1[v1] + path2[v2] + path3[N]
dist2 = path1[v2] + path3[v1] + path2[N]
print(min(dist1, dist2) if min(dist1, dist2) < INF else -1)