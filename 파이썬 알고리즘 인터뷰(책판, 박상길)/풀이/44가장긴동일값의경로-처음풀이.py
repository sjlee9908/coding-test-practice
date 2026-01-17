# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = -1

        def dfs(node, val, depth):
            if not node:
                return -1
            else:
                if val == node.val:
                    depth+=1
                    left_depth = dfs(node.left, node.val, depth)
                    right_depth = dfs(node.right, node.val, depth)
                return max(left_depth, right_depth)

        return dfs(root, root.val, depth)