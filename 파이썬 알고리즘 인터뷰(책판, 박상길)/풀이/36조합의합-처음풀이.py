class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def dfs(pick_num, element, target_changed):
            if target_changed == 0:
                res.append(pick_num[:])
                return
            elif target_changed < 0:
                return
            else:
                for i in range(0, len(element)):
                    if target_changed >= element[i]:
                        pick_num.append(element[i])
                        dfs(pick_num, element[i::], target_changed-element[i])
                        pick_num.pop()
        dfs([],candidates, target)
        return res

sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))



