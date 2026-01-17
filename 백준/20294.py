import collections
import sys

sys.setrecursionlimit(10**9)

# input
n, root = map(int, sys.stdin.readline().split())
tree = collections.defaultdict(collections.defaultdict)

visited = collections.defaultdict(bool)
max_length = 0

for i in range(n - 1):
    n1, n2, w = map(int, sys.stdin.readline().split())
    tree[n1][n2] = w
    tree[n2][n1] = w

print(tree)

# process
def find_giga():
    if len(tree[root]) != 1:
        return root, 0

    ex_node = root
    node = root
    root_to_giga = 0

    while len(tree[node]) != 2:
        for next_node in tree[node].items():
            if next_node[0] != ex_node:
                ex_node = node
                node = next_node[0]
                root_to_giga += next_node[0]
    return root_to_giga, node

print(find_giga())

def find_max_leaf_length(start, length):
    pass
