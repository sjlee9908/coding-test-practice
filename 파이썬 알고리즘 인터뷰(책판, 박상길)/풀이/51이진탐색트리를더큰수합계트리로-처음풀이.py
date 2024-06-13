# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ac = 0
    def bstToGst(self, root):
        def dfs(node):
            if node is None:
                return
            dfs(node.right)
            num = node.val
            node.val += self.ac
            self.ac += num
            dfs(node.left)
            return node

        return dfs(root)

