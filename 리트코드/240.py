class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for li in matrix:
            if li[0] <= target <= li[-1]:
                if target in li:
                    return True

