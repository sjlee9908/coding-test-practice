# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    ans = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(n):
            if n is None:
                return 0

            left = dfs(n.left)
            right = dfs(n.right)

            if n.left is not None and n.left.val == n.val:
                left += 1
            else:
                left = 0
            if n.right is not None and n.right.val == n.val:
                right += 1
            else:
                right = 0

            self.ans = max(self.ans, left + right)
            return max(left, right)

        dfs(root)
        return self.ans