import sys

N = int(sys.stdin.readline())
liquids = list(map(int, sys.stdin.readline().split()))

ex_value = sys.maxsize
i = 0
j = N - 1
liquid1 = 0
liquid2 = 0

while i < j:
    now_value = liquids[i] + liquids[j]

    if abs(now_value) < abs(ex_value):
        liquid1 = liquids[i]
        liquid2 = liquids[j]
        ex_value = now_value

    if now_value == 0:
        break

    elif now_value < 0:
        i += 1

    else:
        j -= 1



print(liquid1, liquid2)