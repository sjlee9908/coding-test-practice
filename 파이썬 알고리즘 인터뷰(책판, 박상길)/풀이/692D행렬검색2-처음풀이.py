class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for i in range(0, len(matrix)):
            if(target in matrix[i]):
                return True

        return False