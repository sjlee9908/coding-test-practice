import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
time_list = [0] * (n+1)
dp_table = [-1] * (n+1)


for i in range(1, 1+n):
    li = list(map(int, sys.stdin.readline().split()))
    time_list[i] = li[0]
    graph[i] = li[2:]


dp_table[1] = time_list[1]
def dfs(dest):
    tmp = 0

    if dp_table[dest] != -1:
        return dp_table[dest]

    for before in graph[dest]:
        tmp = max(tmp, dfs(before))

    dp_table[dest] = time_list[dest] + tmp
    return dp_table[dest]


# 그러니까, 7번째 작업의 선행작업이 1,2,3,4,5임, dfs(7)의 값은 100임
# 하지만, 6번째 작업의 선행작업은 없지만 999999999일 수 있음
if graph[n] == []:
    print(max(time_list))
else:
    print(max(map(dfs, range(1, n+1))))
