import collections


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]




