import collections
import sys

#input
tree_node_count = int(sys.stdin.readline())
tree_input = list(map(int, sys.stdin.readline().split()))
deleted_node = int(sys.stdin.readline())

#process
#tree 생성
tree = [[] for _ in range(tree_node_count)]
root = 0
for child, parent in enumerate(tree_input):
    if parent != -1:
        tree[parent].append(child)
    else:
        root = child

#삭제된 노드의 자식 삭제(삭제된 노드는 아직 남아있음)
tree[deleted_node] = []

#bfs(레벨순회)
def bfs():
    #큐 선언
    que = collections.deque()
    que.append(root)
    #리프노드 선언
    leaf_count = 0

    #순회시작
    while len(que) != 0:
        #pop
        now_node = que.popleft()
        #pop된 노드의 자식이 없음 or 현재 노드의 자식이 1개 있는데, 그 그 자식노드가 삭제된 노드임 -> 리프노드
        if (len(tree[now_node]) == 0 or
                (len(tree[now_node]) == 1 and tree[now_node][0] == deleted_node)):
            leaf_count += 1
        #해당 노드의 자식을 append
        for next_node in tree[now_node]:
            que.append(next_node)

    #삭제된 노드는 반드시 리프노드임 -> 1개를 빼주고 return
    return leaf_count-1

print(bfs())