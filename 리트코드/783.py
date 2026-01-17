# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys


class Solution:
    min_diff = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        n1 = root.left
        while n1 is not None and n1.right is not None:
            n1 = n1.right

        if n1 is not None:
            self.min_diff = min(self.min_diff, abs(root.val - n1.val))

        n2 = root.right
        while n2 is not None and n2.left is not None:
            n2 = n2.left

        if n2 is not None:
            self.min_diff = min(self.min_diff, abs(root.val - n2.val))

        self.minDiffInBST(root.left)
        self.minDiffInBST(root.right)

        return self.min_diff
