import collections

t:int = int(input())

for i in range(t):
    tree = collections.defaultdict(int)
    e_count:int = int(input())
    for j in range(e_count-1):
        parent, child = map(int, input().split())
        tree[child] = parent

    v1, v2 = map(int, input().split())

    v1_ans = collections.deque([])
    v2_ans = collections.deque([])
    same_ans = None

    while v1 != v2:
        v1_ans.append(v1)
        v2_ans.append(v2)
        v1 = tree[v1]
        v2 = tree[v2]
        if v1 == v2:
            same_ans = v1
            break
        if v1 in v2_ans:
            same_ans = v1
            break
        if v2 in v1_ans:
            same_ans = v2
            break
    print(same_ans)






