import sys
sys.setrecursionlimit(10 ** 7)

#input
N = int(sys.stdin.readline())  #그리드의 크기
graph = []
for _ in range(N):
    # 그리드 입력, readline으로 입력받으면 \n이 남아있기에 rstrip
    graph.append(sys.stdin.readline().rstrip())

#rg를 별개로 보는 dfs(적록색맹 X)
def rg_not_same_dfs(x, y, color):
    if visited[x][y] == True:
        return

    if color == graph[x][y]: #이전과 현재가 동일할 때만 dfs 수행
        visited[x][y] = True
        for x_diff, y_diff in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
            if 0 <= x+x_diff < N and 0 <= y+y_diff < N:
                rg_not_same_dfs(x+x_diff, y+y_diff, color)

#rg를 별개로 보는 dfs(적록색맹 O)
def rg_same_dfs(x, y, color):
    if visited[x][y] == True:
        return
    
    #이전과 현재가 동일할 때, 이전이 r, g면 현재가 g, r일때 dfs 수행
    if color == graph[x][y] or (color == "R" and graph[x][y] == "G") or (color == "G" and graph[x][y] == "R"):
        visited[x][y] = True
        for x_diff, y_diff in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
            if 0 <= x+x_diff < N and 0 <= y+y_diff < N:
                rg_same_dfs(x+x_diff, y+y_diff, color)

#적록색맹X 수행
rg_not_same_res = 0
visited = [[False] * N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if visited[x][y] == False:
            rg_not_same_res += 1
            rg_not_same_dfs(x, y, graph[x][y])

#적록색맹O 수행
rg_same_res = 0
visited = [[False] * N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if visited[x][y] == False:
            rg_same_res += 1
            rg_same_dfs(x, y, graph[x][y])

print(rg_not_same_res, rg_same_res)

