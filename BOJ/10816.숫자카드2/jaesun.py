import sys

N = int(input())
n = sorted(map(int, sys.stdin.readline().split()))
M = int(input())
m = list(map(int, sys.stdin.readline().split()))

# dictionary 활용
"""
count = {}

for value in n:
    count[value] = (1 if count.get(value, -1) == -1 else count.get(value) + 1)

for value in m:
    print(count.get(value, 0), end=" ")
"""

# binary search 활용 -> 시간초과 
"""


def binary_search(arr, target, start, end, cnt):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return arr[start:end+1].count(target)
        elif target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
    return cnt

for value in m:
    cnt = 0
    print(binary_search(n, value, 0, len(n)-1, cnt), end=" ")
"""

# binary search 활용 + dictionary 

count = {}
for value in n:
    if value in count:
        count[value] += 1
    else:
        count[value] = 1

# def binary_search(arr, target, start, end):
#     if start > end:
#         return 0
#     mid = (start + end) // 2
#     if arr[mid] == target:
#         return count.get(target)
#     elif arr[mid] < target:
#         return binary_search(arr, target, mid+1, end)
#     else:
#         return binary_search(arr, target, start, mid-1)

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return count.get(target)
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for value in m:
    print(binary_search(n, value, 0, len(n)-1), end=" ")

