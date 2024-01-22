import collections

n = int(input())
s = input()

open_idx = 0
stack = collections.deque([])
count = 0

for i in s:
    if i == '(':
        open_idx += 1
        stack.appendleft(i)
    else:
        if open_idx <= 0:
            stack.appendleft(i)
        else:
            open_idx -= 1
            stack.remove('(')
            if len(stack) != 0 and isinstance(stack[0], int):
                stack.appendleft(stack.popleft() + 2)
            else:
                stack.appendleft(2)


max_sum: int = 0
now_sum: int = 0

for i in stack:
    if isinstance(i, int):
        now_sum += i
    else:
        if now_sum > max_sum:
            max_sum = now_sum
        now_sum = 0
if now_sum > max_sum:
    max_sum = now_sum
    now_sum = 0

print(max_sum)
