import heapq


class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        h = []
        for p in people:
            heapq.heappush(h, (-p[0], p[1]))

        res = []
        while h:
            p = heapq.heappop(h)
            res.insert(p[1], [-p[0], p[1]])
        return res
