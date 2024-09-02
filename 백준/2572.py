import sys

#input
N = int(sys.stdin.readline())
colors = list(sys.stdin.readline().split())
M, K  = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(M)]
for _ in range(K):
    A, B, C  = sys.stdin.readline().split()
    A, B = int(A)-1, int(B)-1
    graph[A].append((B, C)) #양방향
    graph[B].append((A, C))

#점수를 저장하는 dp table 선언
dp_table = [[-1] * N for _ in range(K)]

#dfs
def dfs(pos, n): # pos(현재 위치), n(현재 색깔 idx)로 dfs
    # 종료조건 : 색깔을 다 씀
    if n >= len(colors):
        return 0

    # 이미 계산됨
    if dp_table[pos][n] != -1:
        return dp_table[pos][n]

    #점수 계산
    tmp_dp= 0
    for next_pos, color in graph[pos]:
        tmp = 0
        #색깔이 일치하면 10점 추가
        if color == colors[n]:
            tmp = 10
        #다음노드로 넘어감
        tmp_dp = max(dfs(next_pos, n+1) + tmp, tmp_dp)

    dp_table[pos][n] = tmp_dp

    #계산결과
    return dp_table[pos][n]

print(dfs(0, 0))