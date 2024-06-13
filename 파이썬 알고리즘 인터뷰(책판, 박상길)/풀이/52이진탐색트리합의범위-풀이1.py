# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    val = 0
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0
        return (root.val if low <= root.val <=high else 0) + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)