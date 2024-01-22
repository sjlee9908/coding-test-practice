import copy
import math


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        tmp = 1
        ans = []

        for num in nums:
            ans.append(tmp)
            tmp = tmp * num

        tmp = 1

        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i] * tmp
            tmp = tmp * nums[i]

        return ans


print(Solution.productExceptSelf(None, nums = [1,2,3,4]))

