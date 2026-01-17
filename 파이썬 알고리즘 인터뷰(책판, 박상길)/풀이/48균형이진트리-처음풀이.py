import collections


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getheight(node):
            if node is None:
                return 0
            else:
                return max(getheight(node.left), getheight(node.right)) + 1

        dq = collections.deque([root])
        while len(dq) != 0:
            node = dq.popleft()
            if node is None:
                continue
            dq.append(node.left)
            dq.append(node.right)
            diff = getheight(node.left) - getheight(node.right)
            if diff < -1 or diff > 1:
                return False
        return True
