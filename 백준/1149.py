import sys

R = 0
G = 1
B = 2
N = int(sys.stdin.readline())
budgets = []
for _ in range(N):
    r, g, b = map(int, sys.stdin.readline().split())
    budgets.append((r, g, b))

dp = [[0, 0, 0] for _ in range(N)]

for i in range(N):
    dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + budgets[i][R]
    dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + budgets[i][G]
    dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + budgets[i][B]

print(min(dp[N-1]))
