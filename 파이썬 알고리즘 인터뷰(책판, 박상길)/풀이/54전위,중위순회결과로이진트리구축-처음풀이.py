# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = TreeNode(preorder[0], None, None)
        root_index = inorder.index(preorder[0])
        preorder.pop(0)
        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index+1:])
        return root