import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    result = 0
    # for tree in trees:
    #     if tree > mid:
    #         sum += (tree - mid)
    result = sum(tree - mid if tree > mid else 0 for tree in trees)
    if result >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
        