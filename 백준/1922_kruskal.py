"""kruskal"""
import collections
import sys

#input
v_count = int(sys.stdin.readline())
e_count = int(sys.stdin.readline())
e = collections.deque()

for i in range(e_count):
    e.append(tuple(map(int, sys.stdin.readline().split())))


#process - 정렬    
e = collections.deque(sorted(e, key = lambda x: x[2]))

#process - Disjointset 생성
union = list(range(0, v_count+1))
selected_e = 0
weight = 0

#process - kruskal
while selected_e + 1 != v_count:
    now_e = e.popleft()
    start_0 = now_e[0]
    start_1 = now_e[1]

    if now_e[0] == now_e[1]:
        continue

    #DJS에서 start_0의 부모 찾기 
    while union[start_0] != start_0:
        start_0 = union[start_0]

    #DJS에서 start_1의 부모 찾기
    while union[start_1] != start_1:
        start_1 = union[start_1]

    #같은 집합에 속해있는지 검사 -> 속하지 않았으면 신장트리에 간선 추가, 속해있으면, pass
    if start_0 != start_1:
        union[start_1] = now_e[0]
        selected_e+=1
        weight+=now_e[2]

#output
print(weight)

