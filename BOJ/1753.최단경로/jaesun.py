import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = int(1e9)
graph = [[] for _ in range(V + 1)]
distance = [INF]*(V+1)

for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(start):
    q = []
    # heapq.heappush(q, (start,0))
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # v,w = heapq.heappop(q)
        w, v = heapq.heappop(q)
        if distance[v] < w:
            continue
        for i in graph[v]:
            cost = w + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # heapq.heappush(q, (i[0], cost))
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

# 우선순위 큐에서 뽑을 때 앞에서부터 비교하기 때문에 cost 우선으로 로직을 만들어야 시간 복잡도가 보장되며, 잘못된 답에 이르게 될 수도 있다.
# 다익스트라 알고리즘은 루프마다 항상 아직 방문하지 않은 정점 중 시작점으로부터의 거리가 가장 가까운 정점을 뽑아야 한다.
# INF는 항상 (간선 가중치의 최댓값)*(정점 개수 -1)보다 큰 값을 사용해야 된다.
# https://www.acmicpc.net/board/view/34516
