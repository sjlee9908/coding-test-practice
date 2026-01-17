import collections


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        collection = collections.Counter(nums)
        dict_k = collection.most_common(k)
        res = []
        for i in dict_k:
            res.append(i[0])
        return res

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))