# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    val = 0
    def rangeSumBST(self, root, low, high):
        if root is None:
            return
        if root.val < low:
            self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            self.rangeSumBST(root.left, low, high)
        else:
            self.val += root.val
            self.rangeSumBST(root.right, low, high)
            self.rangeSumBST(root.left, low, high)
        return self.val