# https://www.acmicpc.net/problem/1613
import sys

#input
n, k = map(int, sys.stdin.readline().split())
graph = [[False] * n for _ in range(n)]

for i in range(k):
    u, v = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    #그래프 표시, 일방향 그래프
    graph[u][v] = True

#fw 수행
def fw():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] == False:
                    #사건의 순서가 i->k이고 k->j이면, i->j이다
                    graph[i][j] = (graph[i][k] and graph[k][j])

fw()

test_case = int(sys.stdin.readline())
for i in range(test_case):
    u, v = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    #도달가능성 확인
    if graph[u][v] == True: print(-1)   #u->v인 경우
    elif graph[v][u] == True: print(1)  #v->u인 경우
    else: print(0)                      #둘 다 false인 경우
