class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    return res

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))