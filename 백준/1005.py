import sys

sys.setrecursionlimit(99999)
#process
def dfs(dest):
    #dp_table hit
    if dp_table[dest] != -1:
        return dp_table[dest]

    #dp_table miss
    #선행건물이 없는 경우, 자신의 건설시간을 return
    if graph[dest] == []:
        return construct_time[dest]

    #선행건물이 있는 경우, 선행건물들의 최대건설시간을 구함, 그리고 후행건물의 건설시간을 더해 dp_table을 채움
    tmp = construct_time[dest] + max(map(dfs, graph[dest]))
    dp_table[dest] = tmp
    
    # #선행건물이 있는 경우
    # tmp = 0
    # #선행건물들의 건설시간을 구함
    # for ex_build in graph[dest]:
    #     tmp = max(tmp, dfs(ex_build))
    # dp_table[dest] = tmp + construct_time[dest]

    return dp_table[dest]


#input
t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    construct_time = list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(n)]
    dp_table = [-1] * n

    for _ in range(k):
        # list의 인덱스가 0~(건물수-1)이기 때문에 1을 감소해 받았음
        x, y = map(lambda x: int(x)-1, sys.stdin.readline().split())
        graph[y].append(x)

    dest = int(sys.stdin.readline()) - 1
    print(dfs(dest))