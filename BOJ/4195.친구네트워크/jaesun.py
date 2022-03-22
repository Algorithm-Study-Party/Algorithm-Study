import sys

input = sys.stdin.readline
T = int(input())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
        numbers[b] += numbers[a]
        # print(numbers)
        print(numbers[b])
    elif a < b:  # else로 a == b 같을 때까지 해버리면 중복으로 더해진다. a e, e a 이런식으로 들어왔을 때
        parent[b] = a
        numbers[a] += numbers[b]
        # print(numbers)
        print(numbers[a])
    else:         # 따라서 이렇게 따로 빼주거나 print는 밑에서 처리해주기
        print(numbers[a])
    # if a != b:
    #     parent[b] = a
    #     numbers[a] += numbers[b]
    
    #     print(numbers[a])

for _ in range(T):
    F = int(input())
    friends = {}
    parent = [0]*(2*F)
    numbers = [1]*(2*F)
    for i in range(2*F):
        parent[i] = i
    k = 0
    for _ in range(F):
        a, b = input().split()
        if a not in friends:
            friends[a] = k
            k += 1
        if b not in friends:
            friends[b] = k
            k += 1
        idx_a = friends[a]
        idx_b = friends[b]
        union_parent(parent, idx_a,idx_b)
        # print(numbers[find_parent[idx_a]])
        

        
            

