#모르겠음
class Solution:
    def trap(self, height:list[int]) -> int:
        if not height:
            return 0

        res = 0
        height_ex_i = 0

        for i in range(0, len(height)):
            if height_ex_i < height[i]:
                res += height[i]-height_ex_i
            height_ex_i = height[i]

        return res

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))