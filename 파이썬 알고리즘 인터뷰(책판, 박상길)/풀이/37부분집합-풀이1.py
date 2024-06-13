class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(index, path):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])

        dfs(0, [])
        return res
