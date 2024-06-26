class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    result.add(n1)
        return result