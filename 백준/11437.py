import collections
import sys

N = int(sys.stdin.readline())
vtxs = [[] for _ in range(N+1)]
tree = [-1] * (N+1)
visited = [False] * (N + 1)

def setParentMarker(v):
    while v != -1:
        if parentMarker[v] == True:
            return v
        parentMarker[v] = True
        v = tree[v]


for _ in range(N-1):
    v1, v2 = map(int, sys.stdin.readline().split())
    vtxs[v1].append(v2)
    vtxs[v2].append(v1)


que = collections.deque([1])
while len(que) != 0:
    x = que.popleft()
    if visited[x] == True:
        continue
    visited[x] = True
    for child in vtxs[x]:
        que.append(child)
        if visited[child] != True:
            tree[child] = x

# print(tree)

M = int(sys.stdin.readline())
for _ in range(M):
    parentMarker = [False] * (N + 1)
    a, b = map(int, sys.stdin.readline().split())
    setParentMarker(a)
    print(setParentMarker(b))

