import collections
import heapq

t, n = map(int, input().split())

id_dict = collections.defaultdict(int)
q = []

for i in range(n):
    p = tuple(map(int, input().split()))
    q.append([-p[2], p[0]])
    id_dict[p[0]] = p[1]

heapq.heapify(q)

for i in range(t):
    now_p = heapq.heappop(q)
    id_dict[now_p[1]] -= 1
    print(now_p[1])

    now_p[0] += 1

    if id_dict[now_p[1]] != 0:
        heapq.heappush(q, now_p)