import collections
import heapq
import sys


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        weight = [sys.maxsize] * (n+1)

        for time in times:
            graph[time[0]].append((time[1], time[2]))

        q = [(0, k)]

        while q:
            now_node_weight, now_node = heapq.heappop(q)
            if weight[now_node] == sys.maxsize:
                weight[now_node] = now_node_weight
                for next_node, next_node_weight in graph[now_node]:
                    heapq.heappush(q, (next_node_weight+weight[now_node], next_node))

        weight.pop(0)
        max_len = max(weight)
        if max_len == sys.maxsize:
            return -1
        return max_len

print(Solution.networkDelayTime(None, [[2,1,1],[2,3,1],[3,4,1]], 4, 2))