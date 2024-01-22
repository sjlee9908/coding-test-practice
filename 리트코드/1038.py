# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum_of_large = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(n):
            if n is None:
                return

            dfs(n.right)
            print(n.val, self.sum_of_large)
            self.sum_of_large += n.val
            n.val = self.sum_of_large
            dfs(n.left)
            return n

        return dfs(root)

print(Solution.bstToGst())