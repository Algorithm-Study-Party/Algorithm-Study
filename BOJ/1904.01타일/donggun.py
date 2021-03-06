# n = int(input())
#
# dp = [0] * (n + 1)
# dp[0] = 0
# # 1
# dp[1] = 1
# # 11, 00
# dp[2] = 2
# # # 100, 001
# # dp[3] = 3
# # # 0011, 0000, 1001, 1100, 1111
# # dp[4] = 5
# # # 10000, 00100, 00001, 11100, 11001, 10011, 00111
# # dp[5] = 7
# # # 100100, 110000, 100001, 111100, 111001, 110011, 100111, 000011, 001001, 001100, 001111, ?
# # dp[6] = 12
# # # dp[n] = dp[n-1] + dp[n-2]
#
# for i in range(3, n + 1):
#     dp[i] = dp[i - 2] + dp[i - 1]
#     # print(dp)
#
# print(dp[n])

n = int(input())

dp = [0] * n

if n == 1:
    print(1)
else:
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 15746

    print(dp[n-1])