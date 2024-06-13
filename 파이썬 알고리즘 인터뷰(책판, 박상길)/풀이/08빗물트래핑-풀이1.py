class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        res = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        while left < right:
            left_max, right_max = max(left_max,  height[left]), max(right_max, height[right])

            if left_max <= right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
        return res


sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))