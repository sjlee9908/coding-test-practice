s = input()
bomb = input()

dq = []

for i in s:
    dq.append(i)
    if str(i) == bomb[-1]:
        if str("".join(dq[-len(bomb)::])) == bomb:
            del dq[-len(bomb)::]

if len(dq) == 0:
    print("FRULA")

else:
    print("".join(list(dq)))