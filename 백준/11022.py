n=int(input())
li=[]
for i in range(n):
    li.append(tuple(map(int, input().split())))

for i in range(n):
    print('Case #{0}: {1} + {2} ='.format(i+1, li[i][0], li[i][1]), sum(li[i]))