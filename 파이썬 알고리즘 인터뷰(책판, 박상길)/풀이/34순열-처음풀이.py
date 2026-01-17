import sndhdr


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        e = []

        def dfs():
            for i in nums:
                if i not in e:
                    e.append(i)
                    for j in nums:
                        if j not in e:
                            e.append(j)
                            dfs()
                        if len(res) != len(nums)*(len(nums)-1):
                            res.append(e)
                            e=[]
                            dfs()
        dfs()
        return res

sol = Solution()
print(sol.permute([1,2,3]))


