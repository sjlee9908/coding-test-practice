import itertools
import sndhdr


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return list(itertools.permutations(nums))


sol = Solution()
print(sol.permute([1,2,3]))


