import sys

N = int(sys.stdin.readline())
triangle = [[-1] * N for _ in range(N)]

for i in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    for j, n in enumerate(li):
        triangle[i][j] = n

dp_table = [[-1] * (n+1) for n in range(N)]

def dfs(li, n):
    if li == N:
        return 0
    if n > li:
        return 0

    if dp_table[li][n] != -1:
        return dp_table[li][n]

    dp_table[li][n] = max(dfs(li + 1, n), dfs(li + 1, n + 1)) + triangle[li][n]

    return dp_table[li][n]

print(dfs(0, 0))
# print(*triangle, sep = "\n")
# print(dp_table)
