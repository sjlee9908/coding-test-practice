import sys


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def append(self, new_data):
        if new_data > self.data:
            if self.right == None:
                self.right = TreeNode(new_data)
            else:
                self.right.append(new_data)
        else:
            if self.left == None:
                self.left = TreeNode(new_data)
            else:
                self.left.append(new_data)

    def preorder(self):
        if self == None:
            return
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()
        print(self.data)



sys.setrecursionlimit(20000)
root = TreeNode(int(sys.stdin.readline()))
while(True):
    try:
        root.append(int(sys.stdin.readline()))
    except:
        break

root.preorder()
