import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph = []
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A,B,C))

INF = int(1e9)
distance = [INF] * (N+1)

def bf(start):
    distance[start] = 0
    for i in range(N):
        for j in range(M):
            cur = graph[j][0]
            next_node = graph[j][1]
            cost = graph[j][2]
            if distance[cur] != INF and distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                if i == (N-1):
                    return True
    return False

negative_cycle = bf(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])



