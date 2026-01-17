import sys
# 나중에 다시 풀어봐>>>>>>>>>>>>>>
N, M = map(int, sys.stdin.readline().split())
graph = [[sys.maxsize] * N for _ in range(N)]
for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(lambda x: int(x)-1, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

def fw():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = (
                    min(graph[i][j],
                        graph[i][k] + graph[k][j]
                        )
                )

fw()
chic = []
for i in range(N):
    for j in range(i, N):
        dist = 0
        for k in range(N):
            dist += min(graph[k][i], graph[k][j])
        chic.append((dist, i, j))

chic.sort()
print(chic[0][1]+1, chic[0][2]+1, chic[0][0]* 2)