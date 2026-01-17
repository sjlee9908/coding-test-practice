# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def get_height(n):
            if n is None:
                return 0
            return max(get_height(n.left), get_height(n.right)) + 1

        def get_calc(n):
            if n is None or self.ans == False:
                return
            self.ans = True if abs(get_height(n.left) - get_height(n.right)) <= 1 else False
            get_calc(n.left)
            get_calc(n.right)

        get_calc(root)

        return self.ans



