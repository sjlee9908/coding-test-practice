# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    preorder_idx = 0

    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        def make_tree(new_inorder):
            if new_inorder == [] or self.preorder_idx >= len(preorder):
                return None

            node = TreeNode(preorder[self.preorder_idx])
            inorder_idx = new_inorder.index(preorder[self.preorder_idx])

            self.preorder_idx += 1

            node.left = make_tree(new_inorder[:inorder_idx:])
            node.right = make_tree(new_inorder[inorder_idx+1::])

            return node

        return make_tree(inorder)