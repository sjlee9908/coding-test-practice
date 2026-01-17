# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:

        def createTree(num_list):
            if num_list == []:
                return None
            idx = math.ceil(len(num_list) / 2) -1
            n = TreeNode(num_list[idx])

            n.left = createTree(num_list[:idx])
            n.right = createTree(num_list[idx+1:])

            return n

        return createTree(nums)