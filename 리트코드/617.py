# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(n1, n2):
            if n1 is None and n2 is None:
                return None
            elif n1 is None:
                return n2
            elif n2 is None:
                return n1

            n1.val += n2.val
            n1.left = dfs(n1.left, n2.left)
            n1.right = dfs(n1.right, n2.right)

            return n1

        root1 = dfs(root1, root2)
        return root1


