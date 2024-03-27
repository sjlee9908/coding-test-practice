# https://www.acmicpc.net/problem/1719
import copy
import sys

#input
N, M = map(int, sys.stdin.readline().split())
graph = [[sys.maxsize] * (N) for _ in range(N)]  #그래프
path =  [[None] * (N) for _ in range(N)]  #경로표
for _ in range(M):
    u, v, e = map(lambda x: int(x)-1, sys.stdin.readline().split())
    #그래프 기록
    graph[u][v] = e+1
    graph[v][u] = e+1
    #경로표 기록 - 직통인 경우
    path[u][v] = v
    path[v][u] = u
    

#fw 알고리즘
def fw():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    path[i][j] = k  #i에서 j로 가는 경로가 k노드로 인해 변경됨

#path를 후처리함, 이를 수행하기 전 path는 도착노드의 직전노드가 기록되어 있음 -> 따라서 출발노드의 다음 노드까지 거슬러 올라가야함
def post_process_path():
    for i in range(N):
        for j in range(N):
            dst = j
            stopover = path[i][j]
            while dst != stopover:
                dst = stopover
                stopover = path[i][stopover]
            path[i][j] = stopover
                    
#출력
def print_path():
    for i in range(N):
        for j in range(N):
            if i == j: print("-", end =" ")
            else: print(path[i][j] + 1, end = " ")
        print()



fw()
post_process_path()
print_path()