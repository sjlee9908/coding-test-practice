from itertools import combinations

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        list_com = list(combinations(nums, 3))
        set_com = set( tuple(sorted(x)) for x in list_com )

        res = []

        for i in set_com:
            if sum(i) == 0:
                res.append(list(i))
        return res



sol = Solution()
sol.threeSum([2,-8,8,6,-14,-12,11,-10,13,14,7,3,10,-13,3,-15,7,3,-11,-8,4,5,9,11,7,1,3,13,14,-13,3,-6,-6,-12,-15,-12,-9,3,-15,-11,-6,-1,0,11,2,-12,3,-6,6,0,-6,-12,-10,-12,6,5,-4,-5,-5,-4,-11,13,5,-2,-13,-3,-7,-15,8,-15,12,-13,0,-3,6,9,-8,-6,10,5,9,-11,0,7,-15,-8,-3,-4,-6,7,7,-2,-2,-11,3,0,-6,12,0,-13,4,-3,11,-11,1,2,13,8,4,9,-1,-2,5,14,12,5,13,-6,-13,-8,9,1,5,-8,-2,-6,-1])

