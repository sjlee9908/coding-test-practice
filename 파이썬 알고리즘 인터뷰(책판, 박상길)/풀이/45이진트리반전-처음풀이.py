class Solution(object):
    def invertTree(self, root):
        def dfs(root):
            if root is None:
                return
            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)
            return root

        return dfs(root)
