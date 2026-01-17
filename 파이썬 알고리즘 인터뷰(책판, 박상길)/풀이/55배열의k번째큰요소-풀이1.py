import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = list()

        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)