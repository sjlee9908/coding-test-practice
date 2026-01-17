import sys

sys.setrecursionlimit(99999)

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

x = len(s1)
y = len(s2)

dp_table = [[-1] * (y+1) for _ in range(x+1)]

def dfs(x, y):
    if dp_table[x][y] != -1:
        return dp_table[x][y]

    if x == 0 or y == 0:
        return 0

    elif s1[x-1] == s2[y-1]:
        dp_table[x][y] = 1 + dfs(x-1, y-1)
    else:
        dp_table[x][y] = max(dfs(x, y-1), dfs(x-1, y))

    return dp_table[x][y]

print(dfs(x, y))
