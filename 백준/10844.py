import collections
import sys

N = int(sys.stdin.readline())
dp_table = [[0] * (10) for _ in range(N+1)]
dp_table[1] = [1] * 10
dp_table[1][0] = 0


for i in range(0, N):
    tmp = 0
    for j in range(0, 10):
        if j-1 >= 0:
            dp_table[i+1][j] += dp_table[i][j - 1]
        if j + 1 <= 9:
            dp_table[i + 1][j] += dp_table[i][j + 1]

print(sum(dp_table[N]) % 1000000000)