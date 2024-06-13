import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result

