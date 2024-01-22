# import collections
#
# V_count = int(input())
# E_count = int(input())
# E = collections.deque()
#
# for i in range(E_count):
#     E.append(tuple(map(int, input().split())))
#
# E = collections.deque(sorted(E, key= lambda x: x[2]))
#
# E_select = 0
# union = collections.defaultdict(int)
#
# while V_count != E_select+1:
#     now_e = E.popleft()
#
#     if now_e[0] == now_e[1]:
#         now_e = E.popleft()
#
#
#
#
#     E_select += 1


import collections

v_count = int(input())
e_count = int(input())
e = collections.deque()

for i in range(e_count):
    e.append(tuple(map(int, input().split())))

e = collections.deque(sorted(e, key = lambda x: x[2]))

union = [0]
for i in range(1, v_count+1):
    union.append(i)

selected_e = 0
weight = 0

while selected_e + 1 != v_count:
    now_e = e.popleft()
    start_0 = now_e[0]
    start_1 = now_e[1]

    if now_e[0] == now_e[1]:
        continue

    while union[start_0] != start_0:
        start_0 = union[start_0]

    while union[start_1] != start_1:
        start_1 = union[start_1]

    if start_0 != start_1:
        union[start_1] = now_e[0]
        selected_e+=1
        weight+=now_e[2]

print(weight)




