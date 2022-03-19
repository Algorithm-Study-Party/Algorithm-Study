def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]
arr = sorted(arr, key=lambda k: k[2])
parent = [i for i in range(0, n + 2)]
answer = 0
for a in arr:
    start, end, weight = a
    # cycle 확인
    if find_parent(parent, start) == find_parent(parent, end):
        continue
    else:
        answer += weight
        union_parent(parent, start, end)
print(answer)
