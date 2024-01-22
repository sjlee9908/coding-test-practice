# https://www.acmicpc.net/problem/1976
import collections
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = collections.deque()
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
travel_plan = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))

found = [False] * (N)
travel_site = set(travel_plan)
travel_site_count = len(travel_site)
start = travel_plan[0]

def bfs():
    que = collections.deque()
    que.append(start)
    found[start] = True
    now_site = 1

    while len(que) != 0:
        v = que.popleft()

        for i, u in enumerate(graph[v]):
            if u == 1 and found[i] == False:
                que.append(i)
                found[i] = True
                if i in travel_site:
                    now_site += 1
                    if now_site == travel_site_count:
                        return True
    return False

if bfs() == True or travel_site_count == 1:
    print("YES")
else:
    print("NO")




