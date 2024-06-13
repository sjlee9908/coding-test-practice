import collections
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []

        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk


sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))