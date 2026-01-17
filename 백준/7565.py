import sys

M, N = map(int, sys.stdin.readline().split())
graph = []
riped_tomatoes = []
just_tomatoes = 0


for n in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    for m, t in enumerate(li):
        if t == 1: riped_tomatoes.append((m,n))
        elif t == 0: just_tomatoes += 1

    graph.append(li)

day = 0
tmp = []
diff = [
    [1, 0],[-1, 0],[0,1],[0,-1]
]

while len(riped_tomatoes) != 0:
    tmp = []
    day += 1

    for m, n in riped_tomatoes:
        for dm, dn in diff:
            if 0 <= m + dm < M and 0 <= n + dn < N:
                if graph[n + dn][m + dm] == 0:
                    tmp.append((m + dm, n + dn))
                    just_tomatoes -= 1
                    graph[n + dn][m + dm] = 1

    riped_tomatoes = tmp




if just_tomatoes == 0: print(day-1)
else : print(-1)
