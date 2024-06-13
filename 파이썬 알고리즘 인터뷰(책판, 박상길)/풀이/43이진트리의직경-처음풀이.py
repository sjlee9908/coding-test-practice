class Solution(object):
    def diameterOfBinaryTree(self, root):
        def bfs(root):
            if root == None:
                return 0
            return max(bfs(root.left), bfs(root.right)) + 1

        return bfs(root.left) + bfs(root.right)