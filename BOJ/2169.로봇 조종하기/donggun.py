n, m = map(int, input().split())

road = [[0] * m for _ in range(n)]
print(road)
mars = []
for _ in range(n):
    mars.append(list(map(int, input().split())))

print(mars)

dx = [1, 0, 0]
dy = [0, 1, -1]

def search(x, y):

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            print(road[nx][ny])

            if road[nx][ny] < road[x][y] + mars[nx][ny] or road[nx][ny] == 0:
                road[nx][ny] = road[x][y] + mars[nx][ny]
                search(nx, ny)

search(0, 0)

print(road)



