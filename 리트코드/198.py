import collections


class Solution:
    def __init__(self):
        self.tab = collections.defaultdict(lambda : -1)

    def rob(self, nums: list[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        key = sum(nums)
        if self.tab[key] != -1:
            return self.tab[key]

        self.tab[key] = max(
            self.rob(nums[1:]), self.rob(nums[2:]) + nums[0]
        )

        return self.tab[key]

s = Solution()
nums = [2,7,9,3,1]
print(s.rob(nums))
