class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        num_book = {}

        for idx, num in enumerate(numbers):
            num_book[num] = idx

        for idx, num in enumerate(numbers):
            if target-num in num_book.keys():
                return [idx+1, num_book[target-num]+1]

print(Solution.twoSum(None, numbers = [2,3,4], target = 6))