N, H = map(int, input().split())
down = []
up = []

for i in range(N):
    if i % 2 == 0:
        down.append(int(input()))
    else:
        up.append(int(input()))

down = sorted(down)
up = sorted(up)

min_huddle_count = N
count = 0


def binary_search(source, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if source[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


for i in range(1, H + 1):
    down_count = len(down) - binary_search(down, i - 0.5, 0, len(down) - 1)
    top_count = len(up) - binary_search(up, H - i + 0.5, 0, len(up) - 1)
    result = down_count + top_count
    if min_huddle_count == result:
        count += 1
    elif min_huddle_count > result:
        count = 1
        min_huddle_count = result

print("{} {}".format(min_huddle_count, count))
