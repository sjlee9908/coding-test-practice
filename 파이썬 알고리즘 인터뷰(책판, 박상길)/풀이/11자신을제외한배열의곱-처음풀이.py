import copy
import math

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        nums_copy = copy.deepcopy(nums)
        output = []
        for i in nums:
            nums_copy.remove(i)
            output.append(math.prod(nums_copy))
            nums_copy.append(i)
        return output

sol = Solution()
sol.productExceptSelf()



