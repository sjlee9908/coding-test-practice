import sys

n = int(sys.stdin.readline())
nums = list(sys.stdin.readline().split())
m = int(sys.stdin.readline())

dp_table = [[-1] * (len(nums)+1) for _ in range(len(nums)+1)]

def dfs(s, e):
    if dp_table[s][e] != -1:
        return dp_table[s][e]

    elif s+1 == e or s == e:
        dp_table[s][e] = 1

    elif nums[s] != nums[e-1]:
        dp_table[s][e] = 0

    else:
        dp_table[s][e] = dfs(s+1, e-1)

    return dp_table[s][e]



for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dfs(s-1, e))