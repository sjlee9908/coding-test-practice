n = input()
li = []

for i in n:
    li.append(i)

li.sort(reverse=True)
print("".join(li))
