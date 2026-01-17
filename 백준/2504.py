#input
import collections
import sys

brackets = sys.stdin.readline().rstrip()
stack = collections.deque()
stack.append("-")

if len(brackets) == 1:
    print(0)
    exit(0)

for bracket in brackets:
    num = 0
    if bracket in "([":
        stack.append(bracket)

    else:
        num = 0

        if len(stack) > 0 and isinstance(stack[-1], int):
            num = int(stack.pop())

        open_bracket = stack.pop()

        if open_bracket + bracket == "()":
            if num != 0:
                num *= 2
            else:
                num = 2
            if len(stack) > 0 and isinstance(stack[-1], int):
                stack[-1] += num
            else:
                stack.append(num)
        elif open_bracket + bracket == "[]":
            if num != 0:
                num *= 3
            else:
                num = 3
            if len(stack) > 0 and isinstance(stack[-1], int):
                stack[-1] += num
            else:
                stack.append(num)

        else:
            print(0)
            exit(0)


if len(stack) >= 3:
    print(0)
    exit(0)
else:
    print(stack[-1])

