K, N = map(int, input().split())

lan_length = []

for _ in range(K):
    lan_length.append(int(input()))

start = 1
end = max(lan_length)

while start <= end:
    mid = (start + end) // 2
    count = 0
    # print("start: ", start, "end: ", end)
    for len in lan_length:
        count += len // mid
    # print("count: ", count)
    if count >= N:
        start = mid + 1
    else:
        end = mid -1
    # print("-----------------------")

print(end)

# parametric search
"""
최적화 문제(문제의 상황을 만족하는 특정 변수의 최솟값, 최댓값을 구하는 문제)를 결정 문제로 바꾸어 푸는 것
예시) 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제라면 이분 탐색으로 결정 문제를 해결하면서 범위 좁혀나갈 수 있다.
"""

