num = int(input())

count = 0
while num != 0:
    if num % 2 == 1:
        count += 1
    num = num // 2
print(count)