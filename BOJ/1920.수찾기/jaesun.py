N = int(input())
A = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if target == arr[mid]:
            return 1
        else:
            if target > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return 0

A.sort() # 이진검색은 정렬된 리스트의 경우만 가능하고, 정렬을 함수 안에 넣으니 시간초과
for i in m:
    print(binary_search(A, i, 0, len(A)-1))
