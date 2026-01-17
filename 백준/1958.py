import sys

sys.setrecursionlimit(99999)

x = sys.stdin.readline().rstrip()
y = sys.stdin.readline().rstrip()
z = sys.stdin.readline().rstrip()

dp_table = [[[0] * len(z) for _ in range(len(y))] for _ in range(len(x))]

for i in range(len(x)):
    for j in range(len(y)):
        for k in range(len(z)):
            if i == 0 or j == 0 or k == 0:
                dp_table[i][j][k] = 0
            elif x[i] == y[j] == z[k]:
                dp_table[i][j][k] = 1 + dp_table[i-1][j-1][k-1]
            else:
                dp_table[i][j][k] = max(dp_table[i-1][j][k], dp_table[i][j-1][k], dp_table[i][j][k-1])

print(dp_table[len(x) - 1][len(y) - 1][len(z)-1])
