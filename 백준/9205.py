import collections
import sys

def get_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def bfs():
    que = collections.deque()
    que.append(src)

    while len(que) != 0:
        now = que.popleft()
        visited[now] = True


        if get_dist(now, dest) <= 1000:
            return True

        for store in stores:
            if visited[store] == False and get_dist(now, store) <= 1000:
                que.append(store)

    return False




T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    src = tuple(map(lambda x: int(x) + 32768, sys.stdin.readline().split()))
    visited = collections.defaultdict(lambda :False)
    stores = []
    for _ in range(N):
        stores.append(
            tuple(map(lambda x: int(x) + 32768, sys.stdin.readline().split()))
        )
    dest = tuple(map(lambda x: int(x) + 32768, sys.stdin.readline().split()))

    if bfs() == True:
        print("happy")
    else:
        print("sad")

