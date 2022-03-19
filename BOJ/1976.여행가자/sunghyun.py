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

# 도시의 수 입력
n = int(input())

# 여행계획에 속한 도시들의 수
m = int(input())

# 도시의 수에 대한 연결 정보
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
plan = list(map(int, input().split()))

# 부모 테이블 생성 및 초기화
parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i

# 서로소 집합 만들기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i+1, j+1)

check = True
# 여행 계획에 있는 노드의 루트가 동일한지(같은 집합에 있는지)
for i in range(m-1):
    if find_parent(parent, plan[i]) !=  find_parent(parent, plan[i+1]):
        check = False
if check:
    print('YES')
else:
    print('NO')