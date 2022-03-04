def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 원하는 값 찾은 경우 인덱스 반환
        if array[mid] == target:
            return mid
        # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
        elif array[mid] > target:
            end = mid - 1
        # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
        else:
            start = mid + 1

    return None


N = int(input())
cards = map(int, input().split())
M = int(input())
base = map(int, input().split())

cards = sorted(cards)
result = []
for data in base:
    out = binary_search(cards, data, 0, len(cards) - 1)
    if out == None:
        result.append('0')
    else:
        result.append('1')

print(' '.join(result))
