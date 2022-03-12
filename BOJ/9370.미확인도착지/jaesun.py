import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        w, v = heapq.heappop(q)
        if distance[v] < w:
            continue
        for vertex, weight in graph[v]:
            cost = weight + distance[v]
            if cost < distance[vertex]:
                distance[vertex] = cost
                heapq.heappush(q, (cost, vertex))
    return distance


T = int(input())
for _ in range(T):
    n,m,t = map(int, input().split())
    s,g,h = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b,d = map(int, input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))

    destination = []

    for _ in range(t):
        destination.append(int(input()))

    destination.sort()
    
    path1 = dijkstra(s)
    path2 = dijkstra(g)
    path3 = dijkstra(h)

    for dest in destination:
        # m개의 줄 중에서 g와 h 사이의 도로를 나타낸 것이 존재한다. 또한 이 도로는 목적지 후보들 중 적어도 1개로 향하는 최단 경로의 일부이다.
        # 위의 조건 때문에 g와 h사이의 도로의 길이로 접근하지않고 disjkstra(g)[h] 사용가능
        result1 = path1[g] + path2[h] + path3[dest]
        result2 = path1[h] + path3[g] + path2[dest]
        result3 = path1[dest]

        if result3 == result1 or result3 == result2:
            print(dest)


    
        




