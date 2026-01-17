import sys

n=int(sys.stdin.readline().rstrip())
li=[]

for i in range(n):
    li.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    print(sum(li[i]))
