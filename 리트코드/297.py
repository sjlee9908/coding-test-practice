# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = collections.deque([root])
        node_traversal = collections.deque()

        while q:
            now_node = q.popleft()
            if now_node is not None:
                node_traversal.append(str(now_node.val))
                q.append(now_node.left)
                q.append(now_node.right)
            else:
                node_traversal.append("#")

        print(" ".join(node_traversal))
        return " ".join(node_traversal)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "#":
            return None

        data = collections.deque(list(data.split()))
        child_index = 1
        root = TreeNode(int(data[0]))
        q = collections.deque([root])

        while q:
            node = q.popleft()
            if data[child_index] != "#":
                node.left = TreeNode(int(data[child_index]))
                q.append(node.left)
            child_index += 1

            if data[child_index] != "#":
                node.right = TreeNode(int(data[child_index]))
                q.append(node.right)
            child_index += 1

        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))