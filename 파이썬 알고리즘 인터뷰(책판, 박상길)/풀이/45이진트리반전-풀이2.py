import collections

class Solution(object):
    def invertTree(self, root):
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
