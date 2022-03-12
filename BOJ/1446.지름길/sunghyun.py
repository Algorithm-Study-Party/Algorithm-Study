N, D = map(int, input().split())
ji = []
for i in range(N):
    ji.append(list(map(int, input().split())))

distance = [i for i in range(D + 1)]
for i in range(D + 1):
    if i > 0:
        distance[i] = min(distance[i], distance[i - 1] + 1)
    for start, end, local_distance in ji:
        if i == start and end <= D and distance[i] + local_distance < distance[end]:
            distance[end] = distance[i] + local_distance
    print(distance)
print(distance[D])

