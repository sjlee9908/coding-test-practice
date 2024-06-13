# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution(object):
    diffval = sys.maxsize
    def minDiffInBST(self, root):
        if self.diffval == 1:
            return 1

        if root is None:
            return
        self.minDiffInBST(root.left)
        tmp = root.left
        while tmp is not None:
            if self.diffval > abs(root.val-tmp.val):
                self.diffval = abs(root.val-tmp.val)
            tmp = tmp.right
        tmp = root.right
        while tmp is not None:
            if self.diffval > abs(root.val-tmp.val):
                self.diffval = abs(root.val-tmp.val)
            tmp = tmp.left
        self.minDiffInBST(root.right)

        return self.diffval
