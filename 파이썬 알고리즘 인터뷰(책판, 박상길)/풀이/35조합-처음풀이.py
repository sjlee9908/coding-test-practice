class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = list(range(1, n+1))
        pick_num = []
        res = []

        def dfs(element):
            if len(pick_num) == k:
                res.append(pick_num[:])

            else:
                for i in range(0, len(element)):
                    next_num = element[i+1::]
                    pick_num.append(element[i])
                    dfs(next_num)
                    pick_num.pop()

        dfs(nums)
        return res


sol = Solution()
print(sol.combine(4,2))
