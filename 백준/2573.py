import collections
import sys

ROW, COL = map(int, sys.stdin.readline().split())
graph = []
diff = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]

lands = []
for i in range(ROW):
    li = sys.stdin.readline().rstrip()
    for j, s in enumerate(li):
        if s == "L": lands.append((i, j, 0))
    graph.append(li)

max_level = 0
def bfs(start):
    global max_level
    que = collections.deque()
    que.append(start)
    visited = collections.defaultdict(lambda :False)
    row, col, level = start
    visited[row, col] = True

    while len(que) != 0:
        row, col, level = que.popleft()
        max_level = max(max_level, level)

        for rd, cd in diff:
            if 0<=row+rd<ROW and 0<=col+cd<COL and graph[row + rd][col + cd] == "L" and visited[(row+rd,col+cd)] == False:
                visited[(row+rd,col+cd)] = True
                que.append((row+rd, col+cd, level + 1))

for start in lands:
    bfs(start)

print(max_level)