import collections
import sys

N, L, R = map(int, sys.stdin.readline().split())
A = []

for _ in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    A.append(li)

diff = [
    [1, 0], [-1, 0], [0, 1], [0, -1]
]


def bfs(start):
    que = collections.deque()
    que.append(start)
    size = 0
    pop = 0
    association = []

    while len(que) != 0:
        r, c = que.popleft()

        if visited[r][c] == True:
            continue

        pop += A[r][c]
        size += 1
        association.append((r, c))
        visited[r][c] = True

        for dr, dc in diff:
            if 0 <= dr + r < N and 0 <= dc + c < N:
                if L <= abs(A[r][c] - A[dr + r][dc + c]) <= R:
                    que.append((dr + r, dc + c))

    return size, pop, association



def open_line():
    sizes = []
    pops = []
    associations = []

    for r in range(N):
        for c in range(N):
            if visited[r][c] == False:
                size, pop, association = bfs((r, c))

                if size != 1:
                    sizes.append(size)
                    pops.append(pop)
                    associations.append(association)

    return sizes, pops, associations






count = 0
visited = [[False] * N for _ in range(N)]
sizes, pops, associations = open_line()

while len(associations) != 0:
    for idx, association in enumerate(associations):
        new_pop = pops[idx] // sizes[idx]

        for r, c in association:
            A[r][c] = new_pop

    count += 1
    visited = [[False] * N for _ in range(N)]
    sizes, pops, associations = open_line()

print(count)