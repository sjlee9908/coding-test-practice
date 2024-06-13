# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):

        def dfs(li):
            if len(li) == 0:
                return None
            node = TreeNode(li[len(li)//2], dfs(li[0:len(li)//2]), dfs(li[len(li)//2+1: len(li)]))
            return node

        return dfs(nums)