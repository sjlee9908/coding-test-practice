import sys

N, M = map(int, sys.stdin.readline().split())
disjointset = list(range(N+1))
set_size = [1] * (N+1)


for _ in range(M):
    process, a, b = map(int, sys.stdin.readline().split())
    stk = []
    while disjointset[a] != a:
        stk.append(a)
        a = disjointset[a]
    for i in stk:
        disjointset[i] = a


    stk = []
    while disjointset[b] != b:
        stk.append(b)
        b = disjointset[b]
    for i in stk:
        disjointset[i] = b

    if process == 0:
        disjointset[b] = a

    else:
        if a == b:
            print("YES")
        else:
            print("NO")