import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        ans = []

        for idx, (x, y) in enumerate(points):
            heapq.heappush(heap, (x*x + y*y, idx))

        for i in range(k):
            dist, idx = heapq.heappop(heap)
            ans.append(points[idx])

        return ans



