import collections


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c = collections.Counter(nums)
        return c.most_common(1)[0][0]

print(Solution.majorityElement("a", [3,2,3]))