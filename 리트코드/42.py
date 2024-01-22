class Solution:
    def trap(self, height:list[int]) -> int:

        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            if left_max <= right_max:
                water += (left_max - height[left])
                left+= 1
            else:
                water += (right_max - height[right])
                right -=1

        return water







print(Solution.trap(None, [0,1,0,2,1,0,1,3,2,1,2,1]))