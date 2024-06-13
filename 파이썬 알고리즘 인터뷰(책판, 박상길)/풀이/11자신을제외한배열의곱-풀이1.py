class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = []
        p = 1
        for i in range(len(nums)):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output

sol = Solution()
sol.productExceptSelf([1,2,3,4])



