# input
import collections
import sys

n, m = map(int, sys.stdin.readline().split())

graph = collections.defaultdict(collections.deque)
for i in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
#print(graph)


# processing
def graph_traversal(start_point, friend_count):
    if visited[start_point]:
        return
    if friend_count == 5:
        print(1)
        exit(0)
    else:
        visited[start_point] = True
        for next_point in graph[start_point]:
            graph_traversal(next_point, friend_count + 1)
        visited[start_point] = False


for i in range(n):
    visited = collections.defaultdict(bool)
    graph_traversal(i, 1)

print(0)
