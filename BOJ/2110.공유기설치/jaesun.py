N, C = map(int, input().split())

location = []
for _ in range(N):
    location.append(int(input()))

location.sort()

start = 1
end = location[-1] - location[0]

while start <= end:
    mid = (start + end) // 2
    current = location[0]
    count = 1
    for house in location:
        if current + mid <= house:
            count += 1
            current = house
    if count >= C:
        start = mid + 1
    else:
        end = mid - 1

print(end)
    
    

