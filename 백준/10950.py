n=int(input())
li=[]
for i in range(n):
    li.append(tuple(map(int, input().split())))

for i in range(n):
    print(sum(li[i]))