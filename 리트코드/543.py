# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_length = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def traversal(n):
            if n is None:
                return 0
            else:
                return max(traversal(n.left), traversal(n.right)) + 1

        def get_traversal(n):
            if n is None:
                return
            if (traversal(n.left) + traversal(n.right)) > self.max_length:
                self.max_length = (traversal(n.left) + traversal(n.right))

            get_traversal(n.left)
            get_traversal(n.right)

        get_traversal(root)
        return self.max_length


