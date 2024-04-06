import collections
import sys

N, K = map(int, sys.stdin.readline().split())
graph = [[] * N for _ in range(N)]
ques = [collections.deque(), collections.deque()]
init_que = []

for x in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    for y in range(N):
        graph[x].append(li[y])
        if li[y] != 0:
            init_que.append((li[y], x, y))

init_que.sort()
ques[0] = collections.deque(init_que)
S, X, Y = map(lambda x: int(x)-1, sys.stdin.readline().split())
S += 1

diff_x = [-1, 0, 1, 0]
diff_y = [0, -1, 0, 1]

sec = 0

while sec < S and graph[X][Y] == 0:
    while len(ques[sec%2]) != 0:
        virus, x, y = ques[sec%2].popleft()
        for to_x, to_y in zip(diff_x, diff_y):
            if 0 <= x + to_x < N and 0 <= y + to_y < N:
                if graph[x+to_x][y+to_y] == 0:
                    graph[x+to_x][y+to_y] = virus
                    ques[(sec+1)%2].append((virus, x+to_x, y+to_y))
    sec += 1



print(graph[X][Y])
