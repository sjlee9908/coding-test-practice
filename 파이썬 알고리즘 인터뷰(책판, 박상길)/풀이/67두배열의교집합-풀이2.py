import bisect


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = set()
        nums2.sort()

        for n1 in nums1:
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) >0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)

        return result