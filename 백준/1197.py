import collections

e_count, v_count = map(int, input().split())
v = collections.deque()

for i in range(v_count):
    v.append(tuple(map(int, input().split())))

v = collections.deque(sorted(v, key = lambda x: x[2]))

union = [0]
for i in range(1, e_count+1):
    union.append(i)

selected_v = 0
weight = 0

while selected_v + 1 != e_count:
    now_e = v.popleft()
    start_0 = now_e[0]
    start_1 = now_e[1]

    while union[start_0] != start_0:
        start_0 = union[start_0]

    while union[start_1] != start_1:
        start_1 = union[start_1]

    if start_0 != start_1:
        union[start_1] = now_e[0]
        selected_v+=1
        weight+=now_e[2]

print(weight)

