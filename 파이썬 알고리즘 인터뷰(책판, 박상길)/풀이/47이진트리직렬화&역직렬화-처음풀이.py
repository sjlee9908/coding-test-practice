# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Codec:

    def serialize(self, root):
        if root is None:
            return []
        dq = collections.deque()
        li = []
        dq.append(root)

        while len(dq) != 0 or set(dq) == {None}:
            root = dq.popleft()
            if root is None:
                li.append("None")
            else:
                li.append(root.val)
            if root is not None:
                dq.append(root.left)
                dq.append(root.right)

        while li[-1] == "None":
            li.pop()
        print(str(li))
        return str(li)



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        for i in data:
            if i.isdigit() or i == "":














# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))