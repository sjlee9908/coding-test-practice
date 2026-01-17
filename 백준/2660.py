##!!!!!!!!!!!!!!!!!!!
##논리는 맞는데 통과하지 못할 경우, 극단적인 케이스 생각하기(ex: 노드가 2개, 1개)


import sys

N = int(sys.stdin.readline())
graph = [[sys.maxsize] * (N) for _ in range(N)]
scores = [sys.maxsize] * N
while True:
    a, b = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    if a == -2 and b == -2:
        break
    graph[a][b] = 1
    graph[b][a] = 1


def fw():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

fw()
for i in range(N):
    max_score = -1
    for j in range(N):
        if i != j:
            max_score = max(max_score, graph[i][j])
    scores[i] = max_score


min_score = min(scores)
min_score_node = sorted([node+1 for node, score in enumerate(scores) if score == min_score])

print(min_score, len(min_score_node))
print(*min_score_node)




