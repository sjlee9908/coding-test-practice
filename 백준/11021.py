n=int(input())
li=[]
for i in range(n):
    li.append(tuple(map(int, input().split())))

for i in range(n):
    print('Case #{0}:'.format(i+1), sum(li[i]))