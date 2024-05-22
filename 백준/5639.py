import sys
sys.setrecursionlimit(20000)

#Tree 자료구조
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

    def postorder(self):
        if self == None:
            return
        if self.left != None:
            self.left.postorder()
        if self.right != None:
            self.right.postorder()
        print(self.data)

#input
#root 노드 만듬
root = TreeNode(int(sys.stdin.readline()))

while True:
    li = sys.stdin.readline().rstrip()
    #입력이 끝이 아님
    if li != "":
        data = int(li)
        root.append(data)
    #입력 끝
    else:
        break

#생성된 트리를 후위순회로 호출
root.postorder()
