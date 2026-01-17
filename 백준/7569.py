import sys

M, N, H = map(int, sys.stdin.readline().split())
graph = []
riped_tomatoes = []
just_tomatoes = 0

for h in range(H):
    box = []
    for n in range(N):
        li = list(map(int, sys.stdin.readline().split()))
        for m, t in enumerate(li):
            if t == 1: riped_tomatoes.append((m,n,h))
            elif t == 0: just_tomatoes += 1

        box.append(li)
    graph.append(box)

day = 0
tmp = []
diff = [
    [0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0], [-1,0,0]
]

while len(riped_tomatoes) != 0:
    tmp = []
    day += 1

    for m, n, h in riped_tomatoes:
        for dm, dn, dh in diff:
            if 0 <= m + dm < M and 0 <= n + dn < N and 0 <= h + dh < H:
                if graph[h + dh][n + dn][m + dm] == 0:
                    tmp.append((m + dm, n + dn, h + dh))
                    just_tomatoes -= 1
                    graph[h + dh][n + dn][m + dm] = 1

    riped_tomatoes = tmp




if just_tomatoes == 0: print(day-1)
else : print(-1)
