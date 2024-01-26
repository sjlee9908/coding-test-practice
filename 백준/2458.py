import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[False] * n for _ in range(n)]
smaller_than_me = [0] * n
bigger_than_me = [0] * n

for _ in range(m):
    a, b = map(lambda x: int(x)-1, sys.stdin.readline().split())
    graph[a][b] = True


def fw():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

fw()
ans = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            smaller_than_me[j] += 1
            bigger_than_me[i] += 1



for i in range(n):
    if n-1 == smaller_than_me[i] + bigger_than_me[i]:
        ans += 1

print(ans)
