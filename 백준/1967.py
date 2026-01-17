import sys
sys.setrecursionlimit(30000)

n =  int(sys.stdin.readline())
graph = [[] for _ in range(n)]
to_end = [[] for _ in range(n)]

for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().split())
    graph[p-1].append((c-1, w))


def dfs(now_n, now_w):
    for next_n, next_w in graph[now_n]:
        to_end[now_n].append(dfs(next_n, next_w))

    if len(to_end[now_n]) == 0:
        return now_w
    else:
        return max(to_end[now_n]) + now_w

dfs(0, 0)
max_diameter = 0
#print(*to_end)
for i in range(n):
    to_end[i].sort(reverse=True)

    if len(to_end[i]) == 0:
        continue
    elif len(to_end[i]) == 1:
        max_diameter = max(max_diameter, to_end[i][0])
    else:
        max_diameter = max(max_diameter, to_end[i][0] + to_end[i][1])

print(max_diameter)
