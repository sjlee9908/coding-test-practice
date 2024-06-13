class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        res = []
        nums.sort(key=lambda x: len(str(x)))

        start = 0
        end = 0
        ex_len = len(str(nums[0]))
        print(nums)
        for i in range(len(nums)):
            if i == len(nums)-1:
                start = end
                end = i
                ex_len = len(str(nums[i]))
                res += sorted(nums[start:end+1], key=lambda x: str(x), reverse=True)
                break
            if ex_len != len(str(nums[i])):
                start = end
                end = i
                ex_len = len(str(nums[i]))
                res += sorted(nums[start:end], key=lambda x: str(x), reverse=True)
                if str(nums[end+1] > str(nu)



        print(res)
        return "".join([str(x) for x in res])




sol = Solution()
print(sol.largestNumber([3,30,34,5,9]))