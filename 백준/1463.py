import sys
sys.setrecursionlimit(10 ** 4)

N = int(sys.stdin.readline())
dp_table = [sys.maxsize] * (N+1)
dp_table[1] = 0

for n in range(2, N+1):
    if n % 3 == 0: dp_table[n] = min(dp_table[n//3] + 1, dp_table[n])
    if n % 2 == 0: dp_table[n] = min(dp_table[n // 2] + 1, dp_table[n])
    dp_table[n] = min(dp_table[n - 1] + 1, dp_table[n])

print(dp_table[N])


# import sys
# sys.setrecursionlimit(10 ** 4)
#
# N = int(sys.stdin.readline())
# dp_table = [sys.maxsize] * (N+1)
# dp_table[1] = 0
#
# def dfs(n):
#     if dp_table[n] != sys.maxsize:
#         return dp_table[n]
#
#     if n <= 0:
#         return sys.maxsize
#
#     dp_table[n] = min(
#         (dfs(n // 3) if n % 3 == 0 else sys.maxsize) + 1,
#         (dfs(n // 2) if n % 2 == 0 else sys.maxsize) + 1,
#         dfs(n - 1) + 1
#     )
#
#     return dp_table[n]
#
# print(dfs(N))