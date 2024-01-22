import collections


def preorder_traversal(root='A'):
    if root != '.':
        print(root, end="")
        preorder_traversal(tree[root][0])
        preorder_traversal(tree[root][1])


def inorder_traversal(root='A'):
    if root != '.':
        inorder_traversal(tree[root][0])
        print(root, end="")
        inorder_traversal(tree[root][1])


def postorder_traversal(root='A'):
    if root != '.':
        postorder_traversal(tree[root][0])
        postorder_traversal(tree[root][1])
        print(root, end="")


node_count = int(input())
tree = collections.defaultdict(list)

for i in range(0, node_count):
    root_node, left_child, right_child = input().split(" ")
    tree[root_node] = [left_child, right_child]

#print(tree)
preorder_traversal()
print()
inorder_traversal()
print()
postorder_traversal()

