import collections

class Solution(object):
    def invertTree(self, root):
        stack  = collections.deque([root])

        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left
        return root

