import collections


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = collections.Counter(nums)
        return [x[0] for x in counter.most_common(k)]


print(Solution.topKFrequent(None, nums = [1,1,1,2,2,3], k=2))

