# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return None
            if node1 is None and node2 is not None:
                node2.left = dfs(None, node2.left)
                node2.right = dfs(None, node2.right)
                return node2
            elif node1 is not None and node2 is None:
                node2 = TreeNode(node1.val)
                node2.left = dfs(node1.left, None)
                node2.right = dfs(node1.right, None)
                return node2
            else:
                node2.left = dfs(node1.left, node2.left)
                node2.right = dfs(node1.right, node2.right)
                node2.val = node2.val + node1.val
                return node2

        root2 = dfs(root1, root2)
        return root2


